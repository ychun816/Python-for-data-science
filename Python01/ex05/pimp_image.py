#!usr/bin/env python3

import numpy as np

def ft_invert(array: np.ndarray) -> np.ndarray:
    """Inverts the color of the image / 反轉影像顏色"""
    return 255 - array  # invert all RGB channels

def ft_red(array: np.ndarray) -> np.ndarray:
    """Keeps only the red channel / 保留紅色通道"""
    result = array.copy()
    result[:, :, 1] = 0  # green = 0
    result[:, :, 2] = 0  # blue = 0
    return result

def ft_green(array: np.ndarray) -> np.ndarray:
    """Keeps only the green channel / 保留綠色通道"""
    result = array.copy()
    result[:, :, 0] = 0  # red = 0
    result[:, :, 2] = 0  # blue = 0
    return result

def ft_blue(array: np.ndarray) -> np.ndarray:
    """Keeps only the blue channel / 保留藍色通道"""
    result = array.copy()
    result[:, :, 0] = 0  # red = 0
    result[:, :, 1] = 0  # green = 0
    return result

def ft_grey(array: np.ndarray) -> np.ndarray:
    """Converts the image to grayscale / 轉灰階"""
    # Average of R,G,B channels
    gray = (array[:, :, 0] + array[:, :, 1] + array[:, :, 2]) // 3
    result = np.stack((gray, gray, gray), axis=2)  # keep 3 channels
    return result
