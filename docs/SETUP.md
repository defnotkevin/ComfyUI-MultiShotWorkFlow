# Run the workflow

## 1. Install and update ComfyUI Desktop

Install ComfyUI Desktop using the [official Desktop guide](https://docs.comfy.org/installation/desktop/overview). Complete its initial setup, launch your local instance and apply available application/runtime updates. This workflow needs recent partner nodes and a Preview Image node with an IMAGE output.

Download this repository as a ZIP and extract it, or clone its published GitHub URL. Keep the repository anywhere convenient. It is a workflow collection, so it does **not** need to be installed into `custom_nodes`.

## 2. Sign in and add credits

Open **Settings → User** and sign in to your Comfy account. Then open **Settings → Workspace → Plan & Credits**, choose a top up, and complete checkout. Purchases and generations use your account. Never put account tokens or API keys in the workflow or repository. See the official [account guide](https://docs.comfy.org/interface/user) and [credits guide](https://docs.comfy.org/interface/credits).

Partner nodes require internet connectivity. Check the currently displayed model names, availability, prices and balance in your installation. The export selects **Opus 5.5**, **Nano Banana Pro** (`gemini-3-pro-image-preview`) and **Seedance 2.5**. If your node dropdown does not offer a saved model, update first. Do not assume a different model produces the same result.

## 3. Install the one custom node dependency

Open ComfyUI Manager, search for **ComfyUI-KJNodes**, install it, and restart ComfyUI. Its repository is [kijai/ComfyUI-KJNodes](https://github.com/kijai/ComfyUI-KJNodes). The workflow uses only its `ImageBatchMulti` node. The Claude, Gemini and Seedance nodes are official partner nodes. They are not supplied by KJNodes.

The exact node classes needed are:

| Class | Source |
| --- | --- |
| `LoadImage`, `LoadVideo`, `PreviewImage`, `SaveVideo` | ComfyUI core |
| `ClaudeNode`, `GeminiImage2Node`, `ByteDance2ReferenceNodeV2` | ComfyUI official partner nodes |
| `ImageBatchMulti` | ComfyUI-KJNodes |

## 4. Load the graph and its media

Drag the **root** `ComfyUIMultiShotWorkflowCoffeeExample.json` into the graph canvas. Resolve missing nodes before running. Do not load the archival copy under `originals/` for the prepared example.

The JSON does not contain image or video bytes. Its loaders refer to filenames. Files previously uploaded to one Comfy Cloud workspace do not automatically appear in someone else's Desktop installation or account.

Use either of these methods:

* **Upload/select manually:** use each Load Image / Load Video node's file chooser to select its corresponding source file. The [asset table](../assets/README.md) maps all eight nodes. Save the graph after replacing filenames.
* **Copy into ComfyUI input:** copy the contents of this repository's `coffeeExample/` directory into `<your ComfyUI directory>/input/coffeeExample/`. The prepared JSON uses paths such as `coffeeExample/coffeCupProp.jpeg`. Find the actual input directory for your Desktop installation. It is not necessarily alongside the Desktop application executable.

Check each loader's preview. The original video must contain the original audio. `subjectRightView` and `subjectForwardView` describe environment views. Do not substitute the generated subject portraits for those environment inputs.

## 5. Review prompts and run

When using the supplied coffee example media, run the provided workflow without changing its prompts, graph, model choices or generation settings. File selection and local path changes are permitted. The adaptation options below apply when using your own appropriately licensed media. See the [media permission statement](../assets/MEDIA_LICENSE.md).

Edit the **Director** Claude nodes 28, 29 and 30 for the three image shots, and node 31 for the video sequence. These nodes supply the actual linked prompts. Text stored inside a connected Nano Banana or Seedance prompt widget is not the active prompt. [Prompt templates](PROMPTS.md) explain the reference order.

The original export's generation settings are mostly retained: Nano Banana Pro uses auto aspect ratio and 1K, and Seedance requests 720p in edit mode. To request landscape shot references explicitly, select 16:9 on all three image nodes. Higher image resolution is an optional quality/cost change, not a prerequisite. In Seedance edit mode the source video's duration and aspect ratio are authoritative. The saved duration value is not a promise of trimming or extension. See the [Seedance node documentation](https://github.com/Comfy-Org/docs/blob/main/built-in-nodes/ByteDance2ReferenceNodeV2.mdx).

Press **Run** when ready to spend credits. An uncached full run makes up to eight partner calls: three image director calls, three image generations, one final director call and one video generation. Review the three image previews and the final saved video.

### Optional: review images before paying for video

The graph has no automatic approval gate. To run just the image stage, set nodes **31 (final Director), 4 (Seedance) and 24 (Save Video)** to **Never/muted** using their node mode controls, leaving the three Preview Image outputs active. Run and review the references. Restore those three nodes to **Always** when ready for video.

The export uses randomized seeds, so a subsequent full run can regenerate upstream images. Fixed seed controls may allow ComfyUI's normal cache to reuse unchanged nodes in the same session, but are not durable storage or a guarantee of identical remote output. For reliable reuse, save approved images, load them with Load Image nodes and connect them directly to both the final Director and Seedance in positions 3, 4 and 5. Disconnect/mute the three generation branches if you no longer want them to run.

## 6. Save outputs

The Save Video node writes the final video to ComfyUI's output location with the `video/ComfyUI` prefix. In a hosted session, use the output's download control to save a local copy.

Preview Image outputs are temporary previews. Download the shot images from their preview menus, or connect Save Image nodes if you want persistent files under ComfyUI's output directory. Save the edited workflow JSON as well. That still does not embed the media files.

## App Mode and Comfy Cloud

The prepared JSON preserves the export's App Mode bindings for media, Director prompts, generation settings and four outputs. After importing, switch to App Mode and verify the bindings in your frontend. The ordinary graph remains available for editing. App Mode here is a configured form. It is not a custom multipage shot review application.

For a public try it link, upload the workflow and required media in Comfy Cloud, verify it runs, and use the available App Mode sharing controls. Check what a recipient can access in a separate session before publishing the link. See [App Mode](https://docs.comfy.org/interface/app-mode). Cloud supports a curated set of custom nodes, so confirm KJNodes availability in the target environment. See [Cloud custom node support](https://support.comfy.org/articles/6791455062-custom-nodes-on-cloud).

## Troubleshooting

| Symptom | Check |
| --- | --- |
| Red/missing `ImageBatchMulti` | Install KJNodes and restart. |
| Missing Claude/Gemini/Seedance node or model | Update runtime/frontend and check current partner availability. |
| Preview Image cannot connect onward | Update ComfyUI to a version supporting its IMAGE output. |
| Missing file / old hash filename | Load the root JSON and select all eight local media files. |
| Prompt edits seem ignored | Edit the upstream Director prompt, or disconnect its STRING link before entering a direct model prompt. |
| Wrong overhead reference | It is Seedance **Image 5**, Image 6 is unconnected. |
| Wrong crop in references | ImageBatchMulti resizes the batch to a common size, inspect crops and match reference aspect ratios where possible. |
| Authentication or credit error | Sign in, check balance and connectivity, then inspect the partner error. |
| Audio or identity changes | These are generative model failures, not guarantees enforced by the graph. Inspect before accepting the output. |

For exact original audio, use a separate editing/muxing step and verify synchronization. This workflow only requests audio preservation in the prompt. It does not copy the original audio stream into the result.
