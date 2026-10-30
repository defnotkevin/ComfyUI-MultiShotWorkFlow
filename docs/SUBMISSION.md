# Submission checklist: Open Source Higgsfield

Requirements checked against the [official competition page](https://comfy.org/open-source-higgsfield/) on October 29, 2026. The listed deadline is **October 30, 2026 at 9:00 a.m. Pacific / noon Eastern**. The organizer's live page and submission form remain authoritative.

## Requirements and current status

| Requirement | Status / action |
| --- | --- |
| Built with ComfyUI | This is a ComfyUI workflow with App Mode metadata. |
| Public GitHub repository with workflow, license and local setup | Files prepared, author must create/publish the public repository and verify its URL. No separate app code is claimed. |
| Open source license | MIT included in LICENSE for the authored workflow/docs/script. |
| Enough instructions to run locally | Setup, node dependencies, source media mapping and prompts included. Required media is included in coffeeExample/. |
| Demo no longer than two minutes | Author to record and link. A longer tutorial is additional, not a replacement. |
| Social post linking to the demo with #OpenSourceHiggsfield | Author to publish and link. Supported platforms listed by the contest include Reddit, X, Instagram, LinkedIn, YouTube and TikTok. |
| Optional try it link, strongly encouraged | Author may publish and verify a Comfy Cloud App Mode link. |
| Lawful, SFW material with appropriate IP/likeness rights | Limited media permission is included. Author must still have the rights needed to publish the supplied files. |
| One entry per person | Confirm this is the intended entry. |
| Explain other models/tools used in demo | Name Claude Opus 5.5, Nano Banana Pro, Seedance 2.5 and KJNodes. |

Hosted partner models are allowed in the main competition. This workflow does **not** qualify as Open Weights Only and does not use LTX, FLUX.3 or MiniMax H3 for those model specific bonuses. Submitting accepts the organizer's stated terms, including featuring the work with credit. Review them before submitting.

## Finish the package

* [x] Include the eight required source files in `coffeeExample/`.
* [x] Add the limited media permission in `assets/MEDIA_LICENSE.md`.
* [ ] Confirm that all included media can lawfully be published under that permission.
* [ ] Run `python3 scripts/validate_submission.py --require-assets`.
* [ ] Import the root JSON into a fresh supported ComfyUI installation and select the source assets.
* [ ] Confirm all partner model selections are available and KJNodes is installed.
* [ ] Run the prepared graph with credits, inspect all three images and the final video, and listen to its audio.
* [ ] If you change settings or wiring during that test, export the final root JSON and rerun validation. Update documentation to match.
* [ ] Record the tested ComfyUI/runtime/frontend/KJNodes versions and result in `docs/VALIDATION.md`.
* [ ] Add the demo, social post, optional tutorial and optional try it URLs to README.md.
* [ ] Publish the repository. Verify the files and links without relying on your signed in workspace.
* [ ] Submit through the official form before the deadline. This repository has not been submitted automatically.

[Competition signup](https://form.typeform.com/to/Ayn9Cwfj) · [Submission form](https://form.typeform.com/to/V1dSQrkS)

## Suggested entry description

ComfyUI MultiShot Workflow turns a coffee drinking performance into a cinematic sequence using image guided camera references. Three Claude directors refine image prompts from ordered identity, prop, pose and environment references. Nano Banana Pro generates a right profile, a coffee drinking POV and an overhead composition. A final Claude director assembles the video direction, and Seedance 2.5 edits the original performance using the five image references and source video. The repository includes the workflow, example prompts and local setup instructions. App Mode exposes the configured inputs and outputs.

Do not describe this submission as a fully autonomous shot planner, a character sheet generator, an exact audio preservation system or a custom multipage review app. Those features are not implemented in the submitted graph.

## Demo outline: target 100–115 seconds

| Approximate demo time | Show |
| --- | --- |
| 0–12 s | Original clip and a few seconds of the final multishot result. |
| 12–28 s | Source identity, mug, environment and pose references, explain why roles are separate. |
| 28–50 s | Claude image prompts and the three Nano Banana outputs. Mention models and credit use. |
| 50–70 s | Five Seedance image slots, Video 1, and the timed prompt. Explain Image 5 is overhead. |
| 70–95 s | Final video with audible output, show the intended cuts. |
| 95–115 s | App Mode and graph view, public repository, setup instructions and license. |

You can edit out generation waits. Do not imply the edited demo is real time generation. A longer tutorial can separately show setup, prompt editing, credit purchase and output downloads.

## Suggested social post

> I built a ComfyUI workflow that turns a coffee drinking video into a cinematic multishot sequence. Claude refines the prompts, Nano Banana Pro creates camera references, and Seedance 2.5 edits the source performance. Workflow, setup and prompts are open source. Demo: ADD_DEMO_URL · GitHub: ADD_PUBLIC_REPOSITORY_URL #OpenSourceHiggsfield

Use links to the actual published result. If the final output social post is also the contest social post, include the demo link and required hashtag there. A link showing only the final video does not explain the workflow by itself.
