#!/usr/bin/env python3

"""Simple image loader for ex02 using Pillow and NumPy.

This loader returns an RGB NumPy array on success or ``None`` on
failure. Errors are printed to stderr for convenience in the simple
exercise scripts.
"""

from PIL import Image
import numpy as np
import sys


def ft_load(path: str) -> np.ndarray | None:
    """Load an image and return an RGB NumPy array, or ``None`` on error.

    Only basic JPG/JPEG images are handled here.
    """
    try:
        img = Image.open(path)
        img = img.convert("RGB")
        arr = np.array(img)
        return arr
    except FileNotFoundError:
        print("Error: File not found.", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return None
