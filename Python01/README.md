
[Back to Index](../README.md)

# Python01 — Exercise index

This folder contains short exercises (ex00..ex05). Each exercise has
its own `README.md` explaining the purpose, the important libraries and
syntax used, and how to run the demo/tester for that exercise.

Prerequisites
- Python 3.10+ (this project uses the ``|`` union type in annotations)
- Install the Python dependencies listed in `requirements.txt`:

```bash
python -m pip install --user --upgrade pip
python -m pip install -r requirements.txt
```

Per-exercise files (open any `exNN/README.md` for details):
- `ex00/README.md` — BMI utilities (give_bmi)
- `ex01/README.md` — 2D array slicing (NumPy)
- `ex02/README.md` — Image loader (Pillow + NumPy)
- `ex03/README.md` — Zoom & grayscale (NumPy + Pillow + matplotlib)
- `ex04/README.md` — Crop / transpose (NumPy + matplotlib)
- `ex05/README.md` — Filters and display (NumPy + matplotlib)

Notes
- Image demos expect sample images such as `animal.jpeg` or
  `landscape.jpg`. If those files are not in the current working
  directory, the loader will try `Python01/srcs/` as a fallback.

---
# ex00 — BMI utilities

Files
- `give_bmi.py` — compute BMI values for lists of heights and weights.
- `tester.py` — simple demo runner that prints results and exit codes.

Key concepts and libraries
- Standard library only: uses `sys` for `argv`/`exit` integration.
- Type hints: `list[int | float]` uses the Python 3.10 `|` union.
- `zip` pairs parallel sequences; list comprehensions compute BMIs.
- Defensive checks: `isinstance` and explicit `raise` for input validation.
- Guarded entry: `if __name__ == '__main__'` keeps the module import-safe.
---
# ex01 — 2D array slicing

Files
- `array2D.py` — helper that slices 2D lists using NumPy.
- `tester.py` — demo runner that prints slices.

Key concepts and libraries
- NumPy (`import numpy as np`) for efficient array representation and
  slicing.
- Convert Python lists to NumPy with `np.array(list_of_lists)`.
- Use `.ndim` and `.shape` to inspect array dimensions.
- Row slicing: `arr[start:end]` follows Python slice semantics; negative
  indices are supported.
- Convert back to Python lists with `.tolist()` when needed.
---
# ex02 — Image loader

Files
- `load_image.py` — loads JPEG images using Pillow and returns an RGB
  NumPy array or `None` on failure.
- `tester.py` — prints the loaded array (or a warning) for quick checks.

Key concepts and libraries
- Pillow (`PIL.Image`) for image I/O: `Image.open(path)` and
  `img.convert('RGB')` normalize channels to R,G,B.
- NumPy for numeric arrays: `np.array(img)` yields a (H, W, C) ndarray.
- Pathlib (`Path`) is used to build a repository-local fallback path
  (`Path(__file__).resolve().parents[1] / 'srcs' / filename`).
- The loader prints errors to stderr and returns `None` instead of
  raising, which simplifies use in small demo scripts.
---
# ex03 — Zoom & grayscale

Files
- `zoom.py` — load an image, convert to grayscale, crop/resize to zoom,
  and display with matplotlib.

Key concepts and libraries
- NumPy for array math and slicing.
- Pillow (`Image.fromarray`) for resizing with resample filters
  (e.g., `Image.BICUBIC`).
- Matplotlib (`plt.imshow`, `plt.show`) for display.
- `rgb[..., :3]` selects the first three channels; `np.dot` with
  luminance weights converts RGB to grayscale efficiently.
- `astype(np.uint8)` converts floats back to 0..255 byte range.
---
# ex04 — Crop / transpose

Files
- `rotate.py` — crop the center square of an image, transpose rows/cols,
  and display with matplotlib.

Key concepts and libraries
- Uses the same loader pattern (Pillow + NumPy) as earlier exercises.
- Cropping uses NumPy slicing to extract a centered square region.
- Transpose (`.T`) swaps axes; for images convert to grayscale first so
  the result is a 2D array that transposes meaningfully.
- Matplotlib is used for display and the code handles interrupts
  gracefully (closes figures on `KeyboardInterrupt`).
---
# ex05 — Filters and display

Files
- `pimp_image.py` — several simple filters (invert, red/green/blue
  channel isolation, grey) and helpers to collect and display results.
- `tester.py` — runs filters on an example image and prints shapes.

Key concepts and libraries
- NumPy operations for image manipulation: color inversion (`255 - arr`),
  channel masking (`arr[:, :, 1] = 0`), and grayscale stacking.
- The module demonstrates process-level helpers: collecting outputs in
  module-level state, using `atexit.register` to show results on exit,
  and a SIGINT handler to close GUI windows on Ctrl+C.
- Be careful with module-level mutable state in larger projects; it's
  fine for small exercise scripts but should be avoided in production.
