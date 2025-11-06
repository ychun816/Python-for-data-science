#! usr/bin/env python3


# Use PIL & NumPy. pathlib/typing are optional for improved typing.
from PIL import Image
import numpy as np
# from pathlib import Path
# from typing import Union


def ft_load(path: str) -> np.ndarray:
    """Load an image file and return it as an RGB NumPy array.

    Keeps previous behaviour of returning an error string on failure to
    avoid changing callers. Prints basic info (format/shape) when the
    image is successfully loaded.
    """
    try:
        # Load the image
        img = Image.open(path)  # put jpg path here?

        # Check supported formats
        if img.format not in ["JPEG", "JPG"]:
            return f"Error: Unsupported image format ({img.format})"

        print(f"The format of the image is: {img.format}")

        # Convert to RGB (handle grayscale or RGBA)
        img = img.convert("RGB")

        # Convert to NumPy array
        img_array = np.array(img)

        # Print shape
        print(f"The shape of image is: {img_array.shape}")

        return img_array

    except FileNotFoundError:
        return "Error: File not found"
    except Exception as e:
        return f"Error: {e}"


# Alternative pathlib/typing variants are purposely omitted to keep the
# solution minimal and aligned with the exercise expectations.
