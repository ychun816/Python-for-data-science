#!/usr/bin/env python3

"""Image loader examples for ex05.

The module provides a simple :func:`ft_load` implementation and an
optional commented example using pathlib/typing for educational
purposes.
"""

from PIL import Image
import numpy as np
import sys
from pathlib import Path


def ft_load(path: str) -> np.ndarray | None:
    """Load an image and return an RGB NumPy array, or ``None`` on error.

    Prints brief info on success and prints an error message to stderr on
    failure.
    """
    try:
        p = Path(path)
        if not p.exists():
            alt = Path(__file__).resolve().parents[1] / "srcs" / p.name
            if alt.exists():
                p = alt

        img = Image.open(p)

        if img.format not in ["JPEG", "JPG"]:
            msg = f"Error: Unsupported image format ({img.format})"
            print(msg, file=sys.stderr)
            return None

        print(f"The format of the image is: {img.format}")

        img = img.convert("RGB")
        img_array = np.array(img)

        print(f"The shape of image is: {img_array.shape}")

        return img_array

    except FileNotFoundError:
        print("Error: File not found", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return None


# Method 2: using pathlib / typing (commented example)
# from pathlib import Path
# from typing import Union
#
# def ft_load(path: Union[str, Path]) -> Union[np.ndarray, None]:
#     """Load an image file and return its pixel data as a NumPy array.
#
#     Args:
#         path (str | Path): The path to the image file (JPG or JPEG).
#
#     Returns:
#         np.ndarray | None: The image pixels as an RGB NumPy array if
#                            successful, or None if an error occurred.
#     """
#     try:
#         image_path = Path(path)
#
#         if not image_path.exists():
#             print("Error: File not found.")
#             return None
#
#         if image_path.suffix.lower() not in [".jpg", ".jpeg"]:
#             print("Error: Unsupported file format. Please use JPG or JPEG.")
#             return None
#
#         img = Image.open(image_path)
#         img = img.convert("RGB")
#         arr = np.array(img)
#
#         print(f"The shape of image is: {arr.shape}")
#         return arr
#     except FileNotFoundError:
#         print("Error: File not found.")
#         return None
#     except Exception as e:
#         print(f"Unexpected error: {e}")
#         return None


def main() -> int:
    """Small demo for ex05 loader to keep the module import-safe.

    The demo attempts to load a few candidate images and prints a
    short message. All exceptions are caught so importing this module
    is side-effect free.
    """
    try:
        candidates = [
            "happydoggie.jpg",
            "animal.jpeg",
            "landscape.jpg",
        ]
        result = None
        for name in candidates:
            result = ft_load(name)
            if result is not None:
                break

        if result is None:
            print(
                "Warning: no example image found among candidates; "
                "skipping demo",
                file=sys.stderr,
            )
        else:
            print(result)
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
