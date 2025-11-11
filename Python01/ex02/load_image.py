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
            # Path(__file__).resolve(): absolute path of this file.
            # .parents[1] goes two levels up (project root).
            # Using / "srcs" / p.name constructs a new Path.
            alt = Path(__file__).resolve().parents[1] / "srcs" / p.name
            if alt.exists():
                p = alt
        if not p.exists():
            raise FileNotFoundError(p)

        # Image.open(p): open image file as a Pillow Image object.
        img = Image.open(p)

        # convert('RGB'): ensure image has three color channels (R,G,B).
        img = img.convert("RGB")

        # np.array(img): convert Pillow Image to a NumPy ndarray.
        arr = np.array(img)

        # The returned array is a 3D NumPy array with shape
        print(f"The shape of image is: {arr.shape}")
        return arr

    except FileNotFoundError:
        # file=sys.stderr: print the error to standard error, not stdout.
        print(f"Error: File not found: {path}", file=sys.stderr)
        return None


def main(argv=None) -> int:

    """Run a simple load_image demo and print the returned value.

    Returns 0 on success, 1 on error.
    """
    argv = argv or sys.argv
    try:
        # Try a few common example filenames so the tester works even when
        # the originally-named sample isn't present in the repository.
        candidates = [
            # "animal.jpeg",
            "landscape.jpg",
        ]
        result = None
        for name in candidates:
            result = ft_load(name)
            if result is not None:
                break

        if result is None:
            print(
                "Warning: no example image found among candidates;"
                " skipping demo",
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

# NOTES ############
# alt = Path(__file__).resolve().parents[1] / "srcs" / p.name
# - builds a fallback path relative to this file (project-local).

# Image.open(p) : open the image file using Pillow.

# img.convert("RGB") : ensure the image has 3 color channels (R,G,B).

# np.array(img) : convert the Pillow Image to a NumPy ndarray.

# file=sys.stderr : print error messages to stderr (not stdout).

# return None : used to signal a failure to the caller.

# About the printed NumPy array (tester output): ###
# - The array has shape (rows, cols, channels), e.g. (257, 450, 3).
# 257 列（高），450 欄（寬），3 個色彩通道（R,G,B）

# - Each innermost triplet is a pixel: [R, G, B] values in 0..255.
# - The dtype is usually uint8 (small integers per channel).
# - NumPy prints the full nested array; for large arrays it
#   truncates the middle with "..." for readability.
# - Printing the array therefore shows rows of pixels; each row
#   contains many [R G B] triplets representing the image colors.
# 「rows」代表影像的高度（像素列數），「cols」代表影像的寬度（像素欄數）。
# 「channels」代表每個像素的通道數，RGB 彩色圖通常為 3（分別是紅、綠、藍）。
# 陣列元素形如 [R, G, B]，每個值通常在 0..255 範圍（dtype 常為 uint8）。
# 例：arr.shape == (257, 450, 3) 表示影像高度 257、寬度 450、3 個通道。
# 存取像素：arr[row, col] 回傳該位置的 [R, G, B]；arr[:, :, 0] 會回傳整張影像的紅色通道。
# 注意：NumPy 對大型陣列列印時會中間用 "..." 省略部分內容，實際資料仍完整存在於陣列中。

####################

# TESTER.PY ########
# from load_image import ft_load

# print(ft_load("landscape.jpg"))

# OUTPUT
# $> python tester.py
# The shape of image is: (257, 450, 3)
# [[[19 42 83]
# [23 42 84]
# [28 43 84]
# ...
# [ 0 0 0]
# [ 1 1 1]
# [ 1 1 1]]]
# $
#
#############################
