# Example prompts

These examples document the supplied workflow. With the included coffee example media, use the workflow as supplied. Instructions for changing prompts or connections apply when using your own appropriately licensed media. See the [media permission statement](../assets/MEDIA_LICENSE.md).

These templates are already populated in the prepared root JSON. Paste each image director template into its **Claude Director** prompt, not the connected image model's inactive saved prompt. The accompanying system prompt tells Claude to return only the requested generation prompt.

For manual image prompting, disconnect Claude from the Nano Banana prompt input and use the User direction paragraph with the ordered reference explanation. The reference batch remains connected to Nano Banana.

The wording retains the author's right profile, coffee POV and overhead directions. Black pants are specified for the overhead view. Reference names are translated to image numbers because models do not necessarily see uploaded filenames.

## Right profile image: Director node 28

```text
Create one precise Nano Banana Pro image editing prompt for a single right profile camera reference. Return only the final image prompt, without commentary, headings, JSON, or quotation marks.

Image 1: original subject identity and white graphic tee shirt. Image 2: the environment seen from a camera on the subject's right. It is an environment reference, not a photograph of the subject's profile.

User direction: Imagine the camera on the right side of the subject, capturing the right side profile of the person. Keep all the present elements from the references consistent.

Preserve the face, hairstyle, skin tone, shirt graphic, chair, table, and room landmarks. Specify a camera at the subject's right side, showing the right cheek and ear. Do not mirror the room. Produce one photographic scene, not a character sheet or collage. Use Image 1 for identity and Image 2 for environment. Do not invent a different wardrobe or extra people.
```

## Coffee POV image: Director node 29

```text
Create one precise Nano Banana Pro image editing prompt for a single first person coffee drinking reference. Return only the final image prompt, without commentary, headings, JSON, or quotation marks.

Image 1: the original mug close up, authoritative for shape, handle and decoration. Image 2: the subject drinking, authoritative for right hand grip and cup orientation. Image 3: the subjectForwardView environment, authoritative for the background.

User direction: Imagine what it would look like for the camera to be placed in front of the person's mouth, taking a look inside the coffee cup with some of the coffee leaned against the inner wall of the cup. Don't show any mouth parts like lips, tongue, or teeth. This is a close up shot that keeps the design of the cup consistent. The camera is looking at the edge of the coffee cup from the perspective of the person looking at their forward view. The person is holding the coffee cup in their right hand. The background should be the subjectForwardView.

Resolve the camera as a first person view near the subject's eye/mouth position, looking outward and downward into the tilted cup, not a camera inside the cup looking back at the person. Keep the right hand and physically plausible liquid surface. Refer to Image 3 explicitly for the background. Filenames are not automatically visible to the image model. Produce one photographic image, not a collage.
```

## Overhead image: Director node 30

```text
Create one precise Nano Banana Pro image editing prompt for a single overhead camera reference. Return only the final image prompt, without commentary, headings, JSON, or quotation marks.

Image 1: forAboveShot, showing the actual subject looking up, authoritative for identity, shirt, head tilt, and hand pose. Image 2: subjectTopView, showing the chair, table and floor from above, authoritative for environment geometry.

User direction: Imagine that the camera is right above the person and they are looking into the camera. Imagine what the camera would see from that angle. Make sure to include the slight head tilt in the subject's pose. Include a little bit of coffee in the coffee mug. The subject is wearing black pants. Keep the same hand positions as the reference image where the character is looking up.

Preserve the original face, hair, white graphic tee shirt, black pants, chair and table. Change the viewpoint rather than redesigning the subject. Keep the mug on the table with a little coffee. Do not move it into a hand. Produce one photographic scene, not a collage. Do not invent hands or body details that are hidden in the references.
```

## Final video: Director node 31

This Director gets five images, not the source video. The supplied timing is a user plan, not automatic video analysis.

```text
Refine the following direction into one final Seedance 2.5 video editing prompt. Return only the final prompt, without commentary, headings outside the prompt, JSON, or quotation marks. You receive five ordered reference images but not the source video itself. Do not claim you have watched it. Preserve the specified timing and reference indices. Do not invent dialogue or additional actions. These timestamps are a user supplied plan for an approximately 18 second source clip.

Edit the connected source video into an approximately 18 second cinematic sequence. Keep the original audio and performance timing throughout. Keep character identity, white graphic tee shirt, props, room layout, and lighting consistent. Do not add dialogue or change the performance speed.

Reference roles: Image 1 is the original character identity. Image 2 is the original mug. Image 3 is the generated right profile composition. Image 4 is the generated first person coffee POV. Image 5 is the generated overhead composition. Video 1 is the original performance and timing reference. Use references for their assigned roles. Do not display them as panels.

(0-4 seconds) The camera stays at the default angle and position of Video 1.
(4-7 seconds) Cut to Image 4's close up first person POV of drinking coffee with the right hand. Do not show lips, tongue, or teeth. Match the original drinking action and cup design.
(7-11 seconds) Cut back to a view across the white table, then slowly crane up and move toward the character. Keep the room geometry stable.
(11-15 seconds) Cut to a camera directly above the character, matching Image 5. Preserve the upward gaze, slight head tilt, and source action timing.
(15-18 seconds) Cut to the character's right profile, matching Image 3. Continue the original performance through the source clip's end.

Use clean cuts between these shots. Do not repeat gestures, add extra people, or morph between viewpoints. The source duration is authoritative. Do not extend the video.
```

## Direct Seedance prompt

To use this exact text without Claude rewriting it, disconnect node 31 from the Seedance prompt input, then paste the following. All five image references and Video 1 remain connected.

```text
Edit the connected source video into an approximately 18 second cinematic sequence. Keep the original audio and performance timing throughout. Keep character identity, white graphic tee shirt, props, room layout, and lighting consistent. Do not add dialogue or change the performance speed.

Reference roles: Image 1 is the original character identity. Image 2 is the original mug. Image 3 is the generated right profile composition. Image 4 is the generated first person coffee POV. Image 5 is the generated overhead composition. Video 1 is the original performance and timing reference. Use references for their assigned roles. Do not display them as panels.

(0-4 seconds) The camera stays at the default angle and position of Video 1.
(4-7 seconds) Cut to Image 4's close up first person POV of drinking coffee with the right hand. Do not show lips, tongue, or teeth. Match the original drinking action and cup design.
(7-11 seconds) Cut back to a view across the white table, then slowly crane up and move toward the character. Keep the room geometry stable.
(11-15 seconds) Cut to a camera directly above the character, matching Image 5. Preserve the upward gaze, slight head tilt, and source action timing.
(15-18 seconds) Cut to the character's right profile, matching Image 3. Continue the original performance through the source clip's end.

Use clean cuts between these shots. Do not repeat gestures, add extra people, or morph between viewpoints. The source duration is authoritative. Do not extend the video.
```

## Why these details matter

The original draft had uncovered intervals between 4–5, 7–8 and 15–16 seconds. The prepared plan uses contiguous boundaries. The overhead reference is **Image 5**, not Image 6, because that is where the generated overhead image is actually wired.

The coffee POV is described as looking into a tilted cup from near the person's face. A literal camera inside the cup looking outward would be a different composition. The prompts distinguish these views and preserve the right hand grip.

“Keep the audio the same” is a model instruction, not an exact audio copy operation. Listen to the output. For a different performance, update the shot times to match its gestures and dialogue rather than copying the coffee timing unchanged.

Machine readable copies of the image director templates and direct Seedance prompt are in [example prompts.json](example-prompts.json).
