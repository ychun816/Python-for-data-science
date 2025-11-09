# #!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

from load_image import ft_load
from PIL import Image
import sys


def rgb2gray(rgb) -> np.array:
    """
    Turns a RGB image to Grayscale

    Parameters:
    rgb (np.array): the 2D numpy array representation of the image.

    Return value:
    np.array: the 2D numpy array representation of the grayscale image.
    """
    # Compute luminance and convert to uint8 so printed values match
    # the exercise expected integer pixel values (0..255).
    gray = np.dot(rgb[..., :3], [0.2989, 0.5870, 0.1440])
    # Clip to valid byte range and cast to uint8
    gray = np.clip(gray, 0, 255)
    return gray.astype(np.uint8)


def ft_zoom(path: str, zoom_size: int = 400, zoom: float = 1.0):
    """
    Zooms on an image.

    Parameters:
    path (string): the path of the image to be rotated.

    Return value:
    np.array: The zoomed image as a 2D numpy array
    """
    try:
        img = ft_load(path)
        print(img)

        if img is None:
            print(f"Error: could not load image: {path}", file=sys.stderr)
            return

        img = rgb2gray(img)  # converting image to greyscale (uint8)

        # Support 2D grayscale image
        h, w = img.shape  # unpacking image height and width

        # Zoom logic: zoom >= 1.0 means zoom in (crop smaller area,
        # then resize back to zoom_size). For zoom < 1.0 we treat as
        # 1.0.
        if zoom <= 0:
            zoom = 1.0
        zoom = max(1.0, float(zoom))

        # Compute the crop size in source pixels: smaller crop -> larger
        # zoom.
        crop_h = int(round(zoom_size / zoom))
        crop_w = int(round(zoom_size / zoom))

        # Clamp crop size to image dimensions
        crop_h = min(crop_h, h)
        crop_w = min(crop_w, w)

        # Compute centered start coordinates for the crop
        start_y = max(0, (h - crop_h) // 2)
        start_x = max(0, (w - crop_w) // 2)

        # Centered crop
        cropped = img[start_y:start_y + crop_h, start_x:start_x + crop_w]

        # If crop is same size as desired output, keep it; otherwise
        # resize the cropped region back to the requested zoom_size.
        if (crop_h, crop_w) != (zoom_size, zoom_size):
            pil = Image.fromarray(cropped)
            pil = pil.resize((zoom_size, zoom_size), resample=Image.BICUBIC)
            img_out = np.array(pil).astype(np.uint8)
        else:
            img_out = cropped

        # Ensure the output has a channel axis so printing matches
        # the expected nested single-element values (H, W, 1).
        if img_out.ndim == 2:
            img_out = img_out[:, :, np.newaxis]

        # Print both the (H, W, 1) form and the squeezed (H, W) form
        s1 = img_out.shape
        s2 = img_out.squeeze().shape
        print(f"New shape after slicing: {s1} or {s2}")
        print(img_out)

        plt.imshow(img_out, cmap=plt.get_cmap('gray'))
        plt.show()

    except KeyboardInterrupt:
        # User pressed Ctrl-C while an interactive window was open.
        # Close any open figure and return cleanly instead of letting
        # the KeyboardInterrupt propagate with a long traceback.
        try:
            plt.close()
        except Exception:
            pass
        print("Interrupted by user (KeyboardInterrupt)", file=sys.stderr)
        return
    except Exception as e:
        # Print other errors to stderr and return an error code-like value
        print(f"Error: {e}", file=sys.stderr)
        return


if __name__ == "__main__":
    # Try a couple of common example filenames so the script prints
    # the expected output when run directly.
    candidates = [
        "animal.jpeg",
        # "landscape.jpg",
    ]
    for name in candidates:
        try:
            ft_zoom(name)
            break
        except SystemExit:
            # ft_zoom may call exit() on error; try next candidate
            continue
        except Exception:
            continue

# NOTES
#
# This module provides a simple zoom helper for images. Usage:
#
# - rgb2gray(rgb) -> np.ndarray
#   Convert an RGB image (H x W x 3) to a grayscale 2D uint8 array
#   using standard luminance weights. The result is clipped to 0..255.
#
# - ft_zoom(path: str, zoom_size: int = 400, zoom: float = 1.0)
#   Load the image at ``path`` using ``ft_load`` (from the exercise
#   loader), convert it to grayscale, crop a centered region according
#   to ``zoom`` and resize that crop to ``zoom_size``. The function
#   prints the input and resulting array shapes and displays the image
#   with matplotlib. The printed shape is (H, W, 1) for compatibility
#   with the exercise tester output.
#
# Notes on parameters and behavior:
# - ``zoom`` >= 1.0 zooms in; values <= 0 are treated as 1.0.
# - If the requested crop is larger than the image, the crop size is
#   clamped to the image dimensions and the result is scaled up as
#   necessary.
# - The function handles KeyboardInterrupt (Ctrl+C) by closing any
#   open matplotlib figure and exiting cleanly.
#
# Example (run directly):
#   python zoom.py
#

# Output (example):
#   The shape of image is: (768, 1024, 3)
#   New shape after slicing: (400, 400, 1) or (400, 400)
