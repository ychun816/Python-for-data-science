#!/usr/bin/env python3

from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def ft_zoom(image_array: np.ndarray, zoom_size: int = 400):
    try:
        h, w, c = image_array.shape
        start_x = w // 2 - zoom_size // 2
        start_y = h // 2 - zoom_size // 2
        zoomed = image_array[
            start_y:start_y + zoom_size,
            start_x:start_x + zoom_size,
            :,
        ]

        print(f"New shape after slicing: {zoomed.shape}")
        print(zoomed)
        return zoomed

    except Exception as e:
        print(f"Error: {e}")


def ft_display(image_array: np.ndarray, title="Zoomed Image"):
    plt.imshow(image_array)
    plt.title(title)
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.show()


def main(argv=None) -> int:
    """CLI demo for zoom: loads the example image and displays a
    zoomed area.

    Returns 0 on success, 1 on error. Exceptions are caught so no
    exception escapes at import time.
    """
    import sys

    argv = argv or sys.argv
    try:
        array = ft_load("animal.jpeg")
        if array is not None:
            zoomed = ft_zoom(array, 400)
            ft_display(zoomed)
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    import sys

    sys.exit(main())
# Ensure single newline at EOF


# OUTPUT (example)
# The shape of image is: (768, 1024, 3)
