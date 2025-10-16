#! usr/bin/env python3

from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np

#zoom
def ft_zoom(image_array: np.ndarray, zoom_size: int = 400):
    try:
        h, w, c = image_array.shape
        start_x = w // 2 - zoom_size // 2
        start_y = h // 2 - zoom_size // 2
        zoomed = image_array[start_y:start_y+zoom_size, start_x:start_x+zoom_size, :]
        
        print(f"New shape after slicing: {zoomed.shape}")
        print(zoomed)
        return zoomed
    
    except Exception as e:
        print(f"Error: {e}")

#display 
def ft_display(image_array: np.ndarray, title="Zoomed Image"):
    plt.imshow(image_array)
    plt.title(title)
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.show()

#main
if __name__ == "__main__":
    array = ft_load("animal.jpeg")

    if array is not None:
        zoomed = ft_zoom(array, 400)
        ft_display(zoomed)


#OUTPUT
# The shape of image is: (768, 1024, 3)
# [[[120 111 132]
# [139 130 151]
# [155 146 167]
# ...
# [120 156 94]
# [119 154 90]
# [118 153 89]]]
# New shape after slicing: (400, 400, 1) or (400, 400)
# [[[167]
# [180] [194]
# ... [102]
# [104]
# [103]]]
# $>