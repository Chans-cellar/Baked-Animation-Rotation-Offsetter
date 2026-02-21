## Baked-Animation-Rotation-Offsetter
This is an in-house Python tool developed for Autodesk Maya to resolve rotation offset issues in bat socket joints when exporting baked animations to Unity.

During animation transfer from Maya to Unity, the bat socket exhibited consistent rotational offsets per frame due to coordinate system and transform evaluation differences. This tool corrects that issue by applying a controlled rotation offset on every animation frame, ensuring the final baked animation behaves identically inside Unity.

### Key Features

- Corrects bat socket rotation offsets on baked animations
- Applies per-frame rotation compensation for consistent results
- Designed for Maya → Unity animation pipelines
- Works on already baked animation data
- Simple and artist-friendly Qt-based UI

### Technical Details

- Language: Python

- DCC: Autodesk Maya

- UI Framework: Qt Designer + PySide

- Animation Handling: Frame-by-frame rotation offset application

- Target Engine: Unity (baked animation workflow)

### Use Case

This tool was originally developed during my internship at Behaviol to fix animation inconsistencies in production assets before exporting to Unity, reducing manual cleanup and re-baking time.

### Workflow Overview

1. Load the animated asset in Maya

2. Open the tool via the provided UI

3. Select the bat socket joint

4. Apply the required rotation offset

5. Export baked animation to Unity with corrected transforms
