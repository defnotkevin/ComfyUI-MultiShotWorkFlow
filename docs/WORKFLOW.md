# How the workflow works

This graph makes **three new shot images and one edited video**. It uses original character and mug images directly as identity and prop references. It does not generate character sheets or prop sheets, analyze the source video's timing with Claude, or choose a variable number of shots automatically.

## Reference preparation

| Branch | Ordered images | Director | Image generator | Preview |
| --- | --- | --- | --- | --- |
| Right profile | Character identity, right side environment | 28 | 11 | 12 |
| Coffee POV | Mug, drinking pose, forward environment | 29 | 16 | 17 |
| Overhead | Subject looking up, overhead environment | 30 | 22 | 23 |

Each ImageBatchMulti combines the source images into an ordered batch. Both the branch's Claude node and Nano Banana node receive that batch. Claude translates the supplied direction into a more explicit image editing prompt. Nano Banana receives the reference images plus that text and generates a single composition. The batch node may resize/crop images to a common shape, so preview the source crops when adjusting references.

The overhead branch deliberately has two connected inputs. An additional empty batch slot would not provide useful visual evidence. Reference numbering in each branch is local to that branch. It is different from the final Seedance image numbering.

## Video direction and reference mapping

The final Director (31) receives the two original references and three generated compositions. It refines the supplied sequence instructions. It receives **images only**, not the source video. Timestamps must be supplied by the user and checked against the performance.

| Seedance input | Connected asset | Role |
| --- | --- | --- |
| Image 1 | Original character image, node 1 | Identity, hair and wardrobe |
| Image 2 | Original mug, node 7 | Mug design and proportions |
| Image 3 | Generated right profile through preview 12 | Side view framing |
| Image 4 | Generated coffee POV through preview 17 | First person close up |
| Image 5 | Generated overhead through preview 23 | Top down composition |
| Image 6 | Unconnected | Not referenced by the prompt |
| Video 1 | Original video, node 6 | Performance, timing and source audio |

Seedance (4) receives those references and the final Director's text, then sends the edited video to Save Video (24). The expected timing plan is:

| Time | Intended shot |
| --- | --- |
| 0–4 seconds | Original camera position |
| 4–7 seconds | Coffee drinking POV, Image 4 |
| 7–11 seconds | View across the white table, slowly craning up toward the subject |
| 11–15 seconds | Direct overhead, Image 5 |
| 15–18 seconds | Right profile, Image 3 |

This is a gap free plan. The end of one interval is the start of the next. The source clip is approximately 18 seconds. Use its actual duration rather than extending it to fill a written timestamp. Seedance may approximate cuts, motion and timing.

## Where to change the result

The following modifications apply when using your own appropriately licensed media. The supplied coffee example media is restricted to testing and demonstrating the unchanged workflow under the [media permission statement](../assets/MEDIA_LICENSE.md).

* Change branch Director text to change an image composition. The instructions explicitly bind each source image to an identity, pose, prop or environment role.
* Change the final Director text to change the sequence. Keep its image numbering aligned with the wiring.
* To use a fully manual prompt, disconnect the Director's STRING output from that generation node and enter the desired text in the model's own prompt input. See the direct Seedance example in [PROMPTS.md](PROMPTS.md).
* To reuse an approved image, save it and reconnect a Load Image output to both its final Director slot and its Seedance slot. Updating only one would give the two models different references.

Original face/wardrobe references should remain authoritative. A generated angle is framing guidance. Synthesized views can drift in identity or invent unseen room geometry. A single source image cannot reveal physically accurate hidden detail. Prompting for continuity reduces ambiguity but does not guarantee it.

## Changes from the supplied export

The file in `originals/` retains its original generation graph, with explanatory Markdown notes added. The root submission copy:

1. Replaces workspace specific media names with documented `coffeeExample/` paths.
2. Supplies the three previously empty Claude image director prompts and their system instructions.
3. Makes the final Director's instructions explicit about reference roles and its lack of video input.
4. Uses the latest requested 18 second plan, removes timeline gaps and references overhead as Image 5.
5. Reduces the overhead batch to its two connected inputs and removes three unused generated image loaders.
6. Adds descriptive node titles and removes the batch plumbing controls from the App Mode input list while preserving useful bindings.
7. Keeps named and positional widget settings synchronized so both serialization forms describe the same values.

The root copy requires a fresh ComfyUI test. This package's static checks cannot establish provider availability, account credit, image quality, exact audio preservation or a successful remote render.

## Canvas setup notes

Both workflow JSON files include three MarkdownNote nodes covering account creation and credits, the eight coffee media assignments, and execution and output downloads. These notes have no inputs or outputs and do not change the generation graph. The archived export also explains why users should open the prepared root workflow.
