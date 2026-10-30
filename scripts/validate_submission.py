#!/usr/bin/env python3
"""Validate this packaged ComfyUI graph without importing ComfyUI or making API calls."""
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read_json(path):
    def reject(value):
        raise ValueError(f'Non-finite JSON constant: {value}')
    return json.loads(path.read_text(encoding='utf-8'), parse_constant=reject)


def validate_graph(workflow, manifest):
    errors = []
    def check(condition, message):
        if not condition:
            errors.append(message)
    node_list = workflow['nodes']
    nodes = {node['id']: node for node in node_list}
    check(len(nodes) == len(node_list), 'Duplicate node ID')
    links = {link[0]: link for link in workflow['links']}
    check(len(links) == len(workflow['links']), 'Duplicate link ID')
    edges = {nid: [] for nid in nodes}
    incoming = {nid: 0 for nid in nodes}
    for lid, src, slot, dst, target, kind in workflow['links']:
        if src not in nodes or dst not in nodes:
            errors.append(f'Link {lid}: missing endpoint')
            continue
        outs, ins = nodes[src].get('outputs', []), nodes[dst].get('inputs', [])
        if not (0 <= slot < len(outs) and 0 <= target < len(ins)):
            errors.append(f'Link {lid}: invalid slot')
            continue
        check(lid in (outs[slot].get('links') or []), f'Link {lid}: absent from source output')
        check(ins[target].get('link') == lid, f'Link {lid}: absent from destination input')
        check(outs[slot]['type'] == kind == ins[target]['type'], f'Link {lid}: inconsistent types')
        edges[src].append(dst)
        incoming[dst] += 1
    for nid, node in nodes.items():
        for slot, inp in enumerate(node.get('inputs', [])):
            lid = inp.get('link')
            if lid is not None:
                check(lid in links and links[lid][3:5] == [nid, slot], f'Node {nid}: stale input link {lid}')
        for slot, out in enumerate(node.get('outputs', [])):
            for lid in out.get('links') or []:
                check(lid in links and links[lid][1:3] == [nid, slot], f'Node {nid}: stale output link {lid}')
        named = node.get('widgets_values_named')
        if named is not None:
            check(list(named.values()) == node.get('widgets_values'), f'Node {nid}: named/positional widget mismatch')
        if node['type'] == 'ClaudeNode':
            check(bool(node.get('widgets_values', [''])[0].strip()), f'Node {nid}: empty Director prompt')
        if node['type'] == 'ImageBatchMulti':
            count = node['widgets_values'][0]
            connected = sum(i.get('link') is not None for i in node.get('inputs', []) if i['type'] == 'IMAGE')
            check(count == connected, f'Node {nid}: batch size {count} != connected images {connected}')
    ready = [nid for nid, count in incoming.items() if count == 0]
    visited = 0
    while ready:
        nid = ready.pop()
        visited += 1
        for dst in edges[nid]:
            incoming[dst] -= 1
            if incoming[dst] == 0:
                ready.append(dst)
    check(visited == len(nodes), 'Graph has a cycle')
    for asset in manifest['files']:
        node = nodes.get(asset['node_id'])
        expected = f"{manifest['input_subdirectory']}/{asset['filename']}"
        check(node is not None and node.get('widgets_values', [None])[0] == expected,
              f"Asset mapping mismatch: {asset['filename']}")
    expected_sources = {
        'model.prompt': 31,
        'model.reference_images.image_1': 1,
        'model.reference_images.image_2': 7,
        'model.reference_images.image_3': 12,
        'model.reference_images.image_4': 17,
        'model.reference_images.image_5': 23,
        'model.reference_videos.video_1': 6,
    }
    seedance = nodes.get(4, {})
    for name, source in expected_sources.items():
        inp = next((i for i in seedance.get('inputs', []) if i['name'] == name), {})
        link = links.get(inp.get('link'), [])
        check(bool(link) and link[1] == source, f'Seedance mapping incorrect: {name}')
    for binding in workflow.get('extra', {}).get('linearData', {}).get('inputs', []):
        parts = binding[0].split(':', 2)
        check(len(parts) == 3 and parts[1].isdigit() and int(parts[1]) in nodes,
              f'App Mode input references missing node: {binding[0]}')
    for nid in workflow.get('extra', {}).get('linearData', {}).get('outputs', []):
        check(str(nid).isdigit() and int(nid) in nodes, f'App Mode output references missing node: {nid}')
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workflow', type=Path, default=ROOT / 'ComfyUIMultiShotWorkflowCoffeeExample.json')
    parser.add_argument('--asset-dir', type=Path, default=ROOT / 'coffeeExample')
    parser.add_argument('--require-assets', action='store_true', help='Fail if required media is missing or empty')
    args = parser.parse_args()
    try:
        workflow = read_json(args.workflow)
        manifest = read_json(ROOT / 'assets' / 'manifest.json')
        errors = validate_graph(workflow, manifest)
        prompts = read_json(ROOT / 'docs' / 'example-prompts.json')
        nodes = {n['id']: n for n in workflow['nodes']}
        for nid, text in prompts['image_director_prompts'].items():
            if nodes[int(nid)]['widgets_values'][0] != text:
                errors.append(f'Director {nid}: prompt template differs from workflow')
        if nodes[4]['widgets_values_named']['model.prompt'] != prompts['seedance_prompt']:
            errors.append('Seedance fallback differs from prompt template')
    except (OSError, ValueError, KeyError, TypeError, IndexError) as exc:
        print(f'FAIL: malformed or unreadable package: {exc}')
        return 1
    for name in ['LICENSE', 'README.md', 'docs/SETUP.md', 'docs/PROMPTS.md', 'docs/WORKFLOW.md',
                 'docs/SUBMISSION.md', 'assets/MEDIA_LICENSE.md', 'originals/ComfyUIMultiShotWorkflowCoffeeExample.json']:
        if not (ROOT / name).is_file():
            errors.append(f'Missing package file: {name}')
    missing = [a['filename'] for a in manifest['files'] if a.get('required') and
               (not (args.asset_dir / a['filename']).is_file() or (args.asset_dir / a['filename']).stat().st_size == 0)]
    if args.require_assets:
        errors.extend(f'Missing required media: {name}' for name in missing)
    for error in errors:
        print('FAIL:', error)
    if errors:
        return 1
    print(f"PASS: strict JSON; {len(workflow['nodes'])} nodes; {len(workflow['links'])} reciprocal, typed links; acyclic graph.")
    print('PASS: prompt templates, widget settings, reference mapping, batch counts, App Mode node references and package files.')
    if missing:
        print(f'PENDING: {len(missing)} required media files absent from {args.asset_dir}.')
        for name in missing:
            print('  ' + name)
    else:
        print(f'PASS: all eight required media files exist and are nonempty in {args.asset_dir}.')
    print('NOT TESTED: ComfyUI import/execution, provider availability, paid generations, media fidelity or audio preservation.')
    print('MANUAL: confirm underlying media rights, publish links, record demo and submit the entry.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
