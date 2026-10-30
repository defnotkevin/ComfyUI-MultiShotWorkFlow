# Source media and generated examples

Workflow JSON stores node settings, links and filenames. It does **not** bundle the referenced images or video. The source export resolved those files in the author's Comfy Cloud workspace. A new user needs the files too.

The following eight source files are included in `coffeeExample/` at the repository root. These are the seven original image references plus the original performance video, not just the final social video.

| Loader node | Exact filename | Purpose |
| --- | --- | --- |
| 1 | `coffeeCharacterReference.png` | Original character identity and wardrobe |
| 6 | `CoffeeDrinkLandscape.mp4` | Original performance video with audio |
| 7 | `coffeCupProp.jpeg` | Original mug design and proportions |
| 10 | `subjectRightView.png` | Environment visible from a right side camera |
| 14 | `forCoffeeCupShot.png` | Drinking pose and right hand grip |
| 18 | `subjectForwardView.png` | Environment seen from the subject looking forward |
| 19 | `subjectTopView.png` | Overhead chair, table and floor reference |
| 21 | `forAboveShot.png` | Subject looking up: head tilt and hand pose |

Copy these files into `<ComfyUI>/input/coffeeExample/`, or choose each file manually in its loader after importing the root JSON. Preserve capitalization and the spelling `coffeCupProp.jpeg`. The source media can be found in the author's `coffeeExample` folder before packaging. No personal absolute path is stored in the portable workflow.

The folder also includes these previously generated examples:

* `ComfyRightProfile.png`
* `ComfyCoffeePOV.png`
* `ComfyAbovePOv.png`

These files are visual examples and are not loaded by the prepared graph. Other included images, such as `subjectLeftView.png`, `forSideShots.png` and `CoffeeExample1.png`, are also unused by the prepared graph. All media in this folder is covered by the same limited permission.

The supplied media may be used only to test and demonstrate the provided unchanged workflow. Read [MEDIA_LICENSE.md](MEDIA_LICENSE.md) for the full terms. Modifications described elsewhere in the documentation require your own appropriately licensed media. Do not upload credentials or private Cloud access links.

Run `python3 scripts/validate_submission.py --require-assets` from the repository root after adding the required files. It checks packaging and graph consistency, not media quality or legal rights.

## Sharing on GitHub

The 14 media files currently total approximately 45.13 MiB. The largest file is `CoffeeDrinkLandscape.mp4` at 18.37 MiB. All current files are below both the 25 MiB browser upload limit and the 100 MiB Git upload limit. You can upload through GitHub Desktop, Git or the browser. Git LFS is not required for these files. See [GitHub file limits](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github).

Keep the media permission statement and this guide with the repository. Users can download the repository ZIP or clone it to obtain the workflow and media together. A public repository can be viewed and forked under GitHub's platform terms. The media notice governs the additional permission to use the example assets.
