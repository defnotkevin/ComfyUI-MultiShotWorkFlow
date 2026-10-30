# Validation record

## Static package checks

Performed during submission preparation on October 29, 2026, using Python's standard library. No ComfyUI runtime or partner account was used.

* Strict JSON parsing passed, with nonfinite values rejected.
* The prepared graph has 23 generation and loader nodes, three Markdown notes, and 32 links. Endpoint slots, reciprocal link records and socket types agree. The graph is acyclic.
* Named and positional widget values match, including prompts, source filenames and the overhead batch's two inputs.
* All four Director prompts are populated. Image director templates and the direct Seedance fallback match the documented JSON templates.
* Seedance has the expected five image references and original video. The overhead source is Image 5.
* App Mode bindings refer to existing nodes.
* The validator rejects a deliberately emptied Director prompt and a deliberately broken graph endpoint.
* The archival export retains its original generation nodes, settings and connections. Three explanatory Markdown notes were added on October 30, 2026, so it is no longer a byte for byte copy.
* On October 30, 2026, all eight required source files were verified as present and nonempty in the repository's `coffeeExample/` folder. The folder also contains six optional example or reference images.

Run from the repository root:

```sh
python3 scripts/validate_submission.py
python3 scripts/validate_submission.py --require-assets
```

The first command permits missing media and prints a PENDING list if any are absent. The second requires all eight files under `coffeeExample/` and passes with the supplied folder. You can inspect another source directory with `--asset-dir /path/to/coffeeExample`. Passing that check does not put additional files in the repository.

## Not yet validated

* Import and execution in a fresh ComfyUI Desktop or Cloud session.
* Current account access, provider availability, prices or successful paid generation.
* Visual fidelity, camera timing, right hand continuity or unchanged audio.
* Public repository and demo/social/tutorial links. The requested media permission is now documented, but underlying ownership and third party rights have not been independently verified.

No paid API generation, GitHub publication or competition submission was performed during packaging. The author's earlier reported successful coffee result does not validate the modified submission copy.

## Record the final live test

| Item | Value |
| --- | --- |
| Test date | PENDING |
| Desktop/Cloud and ComfyUI version | PENDING |
| Frontend version actually tested | PENDING (source export records 1.58.0) |
| KJNodes version/commit | PENDING |
| Available partner models selected | PENDING |
| Source assets loaded from fresh checkout | PENDING |
| Three generated references reviewed | PENDING |
| Final video and audio reviewed | PENDING |
| Final exported workflow checksum | PENDING if changed after this preparation |

## Preparation checksums (SHA-256)

These identify the two JSON files after the October 30 setup notes were added. Exporting the workflow again will change its checksum.

* Prepared root workflow: `b5fb152ad43983af5b7b914fa4c8e2ab15cc869334a1fdf2967e966953012580`
* Archived export with notes: `9650e179afc3815f7e32edc8d8175990fe73a0ec637b6c15efb0ef9cb84fd09d`

## Setup documentation check

On October 30, 2026, the README received account and credit instructions followed by a complete coffee setup walkthrough. Three MarkdownNote nodes were added to each workflow. The existing generation nodes, links and App Mode metadata were compared before and after and remain unchanged. Canvas rendering in a live ComfyUI frontend has not been tested.
