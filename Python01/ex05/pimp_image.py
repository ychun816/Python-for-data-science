#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load
import atexit
import signal
import sys
import os

# Module-level collection of original + filtered images. Filters will
# populate these when called so we can display them together later.
_original_image = None
_collected = {}
_displayed = False
_suppress_atexit_display = False

# If this module is imported in a child process that is only intended to
# display the images, we disable the atexit and signal registrations to
# avoid duplicate displays and recursive spawning. The child display
# process will set PIMP_IMAGE_NO_ATEXIT=1 in its environment.
_disable_handlers = os.getenv("PIMP_IMAGE_NO_ATEXIT") == "1"


def _ensure_original(arr: np.ndarray):
    global _original_image
    if _original_image is None:
        # store a copy to avoid accidental modification
        _original_image = np.asarray(arr, dtype=np.uint8).copy()


def _display_collected_once():
    """Create a 3x2 figure showing Original, Invert, Red, Green, Blue, Grey.

    This function is safe to call multiple times but will only display once
    per process run.
    """
    global _displayed
    if _displayed:
        return
    # need at least the original image to display anything
    if _original_image is None:
        return

    names = ["Original", "Invert", "Red", "Green", "Blue", "Grey"]
    # prepare image list in the requested order; fill missing with zeros
    imgs = []
    orig = np.asarray(_original_image, dtype=np.uint8)
    for name in names:
        if name == "Original":
            imgs.append((name, orig))
        else:
            im = _collected.get(name)
            if im is None:
                # placeholder: black image with same shape
                im = np.zeros_like(orig)
            imgs.append((name, np.asarray(im, dtype=np.uint8)))

    fig, axes = plt.subplots(3, 2, figsize=(12, 18))
    axes = axes.flatten()
    for i, (name, im) in enumerate(imgs):
        ax = axes[i]
        ax.imshow(im)
        ax.axis('off')
        label = f"Figure VIII.{i+1}: {name}"
        ax.text(
            0.5,
            -0.08,
            label,
            transform=ax.transAxes,
            ha='center',
            va='top',
            fontsize=10,
        )

    for j in range(len(imgs), len(axes)):
        axes[j].axis('off')

    plt.tight_layout()
    plt.subplots_adjust(hspace=0.35, bottom=0.05)

    try:
        plt.show()
    except Exception:
        # In non-GUI environments this may fail; we ignore it.
        pass

    _displayed = True


def _atexit_display():
    # Display when the process exits normally.
    if _suppress_atexit_display:
        return
    _display_collected_once()


def _sigint_handler(signum, frame):
    # On Ctrl+C, display collected images then exit.
    # Suppress the atexit display and try to close any local matplotlib
    # windows, then exit. We avoid spawning children here to keep behavior
    # predictable: Ctrl+C should prevent or kill the display.
    global _suppress_atexit_display
    _suppress_atexit_display = True
    try:
        plt.close('all')
    except Exception:
        pass
    try:
        signal.signal(signal.SIGINT, signal.SIG_DFL)
    except Exception:
        pass
    try:
        sys.exit(0)
    except SystemExit:
        raise


if not _disable_handlers:
    atexit.register(_atexit_display)
    signal.signal(signal.SIGINT, _sigint_handler)


def ft_invert(array: np.ndarray) -> np.ndarray:
    """Inverts the color of the image / 反轉影像顏色"""
    # invert all RGB channels and return a new array
    result = 255 - array
    try:
        _ensure_original(array)
        _collected["Invert"] = np.asarray(result, dtype=np.uint8)
    except Exception:
        # keep functions robust even if collection fails
        pass
    return result


def ft_red(array: np.ndarray) -> np.ndarray:
    """Keeps only the red channel / 保留紅色通道"""
    result = array.copy()
    result[:, :, 1] = 0  # green = 0
    result[:, :, 2] = 0  # blue = 0
    try:
        _ensure_original(array)
        _collected["Red"] = np.asarray(result, dtype=np.uint8)
    except Exception:
        pass
    return result


def ft_green(array: np.ndarray) -> np.ndarray:
    """Keeps only the green channel / 保留綠色通道"""
    result = array.copy()
    result[:, :, 0] = 0  # red = 0
    result[:, :, 2] = 0  # blue = 0
    try:
        _ensure_original(array)
        _collected["Green"] = np.asarray(result, dtype=np.uint8)
    except Exception:
        pass
    return result


def ft_blue(array: np.ndarray) -> np.ndarray:
    """Keeps only the blue channel / 保留藍色通道"""
    result = array.copy()
    result[:, :, 0] = 0  # red = 0
    result[:, :, 1] = 0  # green = 0
    try:
        _ensure_original(array)
        _collected["Blue"] = np.asarray(result, dtype=np.uint8)
    except Exception:
        pass
    return result


def ft_grey(array: np.ndarray) -> np.ndarray:
    """Converts the image to grayscale / 轉灰階"""
    # Average of R,G,B channels
    gray = (array[:, :, 0] + array[:, :, 1] + array[:, :, 2]) // 3
    result = np.stack((gray, gray, gray), axis=2)  # keep 3 channels
    try:
        _ensure_original(array)
        _collected["Grey"] = np.asarray(result, dtype=np.uint8)
    except Exception:
        pass
    return result


def show_all_filters():
    """Display all filters in a single 3x2 matplotlib window.

    Layout (left-to-right, top-to-bottom):
    Figure VIII.1: Original   Figure VIII.2: Invert
    Figure VIII.3: Red        Figure VIII.4: Green
    Figure VIII.5: Blue       Figure VIII.6: Grey

    This helper does not save any files; it only opens a display window
    (plt.show()). It is safe to call from a script or interactive session.
    """
    arr = ft_load("landscape.jpg")
    if arr is None:
        return 1

    imgs = [
        ("Original", arr),
        ("Invert", ft_invert(arr)),
        ("Red", ft_red(arr)),
        ("Green", ft_green(arr)),
        ("Blue", ft_blue(arr)),
        ("Grey", ft_grey(arr)),
    ]

    imgs = [(name, np.asarray(im, dtype=np.uint8)) for name, im in imgs]

    fig, axes = plt.subplots(3, 2, figsize=(12, 18))
    axes = axes.flatten()

    for i, (name, im) in enumerate(imgs):
        ax = axes[i]
        ax.imshow(im)
        ax.axis('off')
        label = f"Figure VIII.{i+1}: {name}"
        ax.text(
            0.5,
            -0.08,
            label,
            transform=ax.transAxes,
            ha='center',
            va='top',
            fontsize=10,
        )

    for j in range(len(imgs), len(axes)):
        axes[j].axis('off')

    plt.tight_layout()
    plt.subplots_adjust(hspace=0.35, bottom=0.05)

    try:
        plt.show()
    except Exception:
        pass

    return 0


# NOTES
#
# This module provides small image filter functions that operate on NumPy
# arrays representing RGB images (shape: H x W x 3, dtype uint8).
#
# Public functions:
# - ft_invert(array) -> array
#   Returns a new NumPy array with colors inverted (255 - value).
#
# - ft_red(array) -> array
#   Returns a copy of the array with only the red channel kept. The green
#   and blue channels are set to 0.
#
# - ft_green(array) -> array
#   Returns a copy with only the green channel kept.
#
# - ft_blue(array) -> array
#   Returns a copy with only the blue channel kept.
#
# - ft_grey(array) -> array
#   Returns a grayscale version produced by averaging R, G and B values and
#   stacking into a 3-channel uint8 image.
#
# - show_all_filters()
#   Convenience helper that loads the example image (landscape.jpg) and
#   displays Original, Invert, Red, Green, Blue and Grey images in a single
#   3x2 matplotlib window. The function does not write files.
#
# Signal and exit behaviour:
# - When filters are called, the module collects their outputs. On normal
#   interpreter exit the collected images are displayed once (via atexit).
# - Pressing Ctrl+C suppresses the atexit display and attempts to close any
#   open matplotlib windows before exiting. This avoids spawning GUI code
#   during interpreter shutdown which can cause crashes.
############################################################

# TESTER.PY ##################
# from load_image import ft_load
# from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey

# array = ft_load("landscape.jpg")
# if array is not None:

#     print(array)
#     ft_invert(array)
#     ft_red(array)
#     ft_green(array)
#     ft_blue(array)
#     ft_grey(array)
#     print(ft_invert.__doc__)

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
# ...
# Inverts the color of the image received.
# $>

#############################
