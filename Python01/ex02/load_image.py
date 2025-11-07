#!/usr/bin/env python3

"""Simple image loader for ex02 using Pillow and NumPy.

This loader returns an RGB NumPy array on success or ``None`` on
failure. Errors are printed to stderr for convenience in the simple
exercise scripts.
"""

from PIL import Image
import numpy as np
import sys
from pathlib import Path


def ft_load(path: str) -> np.ndarray | None:
    """Load an image and return an RGB NumPy array, or ``None`` on error.

    Only basic JPG/JPEG images are handled here.
    """
    try:
        p = Path(path)
        if not p.exists():
            # Try repository-local fallback: Python01/srcs/<filename>
            alt = Path(__file__).resolve().parents[1] / "srcs" / p.name
            if alt.exists():
                p = alt
        if not p.exists():
            raise FileNotFoundError(p)

        img = Image.open(p)
        img = img.convert("RGB")
        arr = np.array(img)
        return arr
    except FileNotFoundError:
        print(f"Error: File not found: {path}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return None
