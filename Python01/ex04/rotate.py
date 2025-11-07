#!usr/bin/env python3

from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def ft_square_crop(image_array: np.ndarray, size: int = 400):
    """Crop the center square of the image / 裁剪中央正方形"""
    try:
        h, w, c = image_array.shape
        start_x = w // 2 - size // 2
        start_y = h // 2 - size // 2
        square = image_array[start_y:start_y+size, start_x:start_x+size, :]
        print(f"The shape of image is: {square.shape}")
        print(square)
        return square
    except Exception as e:
        import sys

        print(f"❌ Error while cropping: {e}", file=sys.stderr)
        return None


def ft_transpose(image_array: np.ndarray):
    """Transpose image (rows ↔ columns) / 轉置影像"""
    try:
        # If color image, convert to grayscale first (optional)
        if image_array.shape[2] == 3:
            # Convert RGB → grayscale by averaging channels
            gray = np.mean(image_array, axis=2).astype(int)
        else:
            gray = image_array
        transposed = gray.T  # transpose rows ↔ columns
        print(f"New shape after Transpose: {transposed.shape}")
        print(transposed)
        return transposed
    except Exception as e:
        import sys

        print(f"❌ Error while transposing: {e}", file=sys.stderr)
        return None


def ft_display(image_array: np.ndarray, title="Transposed Image"):
    """Display image with axes / 顯示圖片與座標軸"""
    plt.imshow(image_array, cmap='gray')
    plt.title(title)
    plt.xlabel("X-axis / X軸")
    plt.ylabel("Y-axis / Y軸")
    plt.show()


def main(argv=None) -> int:
    """Demo runner for rotate utilities.

    Loads the example image, crops a square and displays the transposed
    result. Returns 0 on success, 1 on error and catches exceptions so none
    escape import-time execution.
    """
    import sys
    argv = argv or sys.argv
    try:
        arr = ft_load("animal.jpeg")
        if arr is not None:
            square = ft_square_crop(arr, 400)
            if square is not None:
                transposed = ft_transpose(square)
                if transposed is not None:
                    ft_display(transposed)
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    import sys

    sys.exit(main())

# OUTPUT
# $> python rotate.py
# The shape of image is: (400, 400, 1) or (400, 400)
# [[[167]
# [180]
# [194]
# ...
# [102]
# [104]
# [103]]]
# New shape after Transpose: (400, 400)
# [[167 180 194 ... 64 50 72]
# ...
# [115 116 119 ... 102 104 103]]
# $>
