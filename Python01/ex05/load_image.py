#! usr/bin/env python3

#use PIL & numPY lib # do i need pathlib and typing? -> to check
from PIL import Image
import numpy as np
# from pathlib import Path
# from typing import Union

def ft_load(path: str) -> np.ndarray:
    try:
        # Load the image
        img = Image.open(path) #put jpg path here? 
        
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

#method2: using pathlib / typing
# from PIL import Image
# import numpy as np
# from pathlib import Path
# from typing import Union

# def ft_load(path: Union[str, Path]) -> Union[np.ndarray, None]:
#     """
#     Load an image file and return its pixel data as a NumPy array.
    
#     Args:
#         path (str | Path): The path to the image file (JPG or JPEG).

#     Returns:
#         np.ndarray | None: The image pixels as an RGB NumPy array if successful,
#                            or None if an error occurred.
#     """
#     try:
#         # Convert to Path object (if not already)
#         image_path = Path(path)

#         #Validate file existence
#         if not image_path.exists():
#             print("Error: File not found.")
#             return None

#         #Validate file format
#         if image_path.suffix.lower() not in [".jpg", ".jpeg"]:
#             print("Error: Unsupported file format. Please use JPG or JPEG.")
#             return None

#         #Load image using Pillow
#         img = Image.open(image_path)

#         #Ensure image is in RGB mode (3 channels)
#         img = img.convert("RGB")

#         #Convert image to NumPy array
#         arr = np.array(img)

#         #Display info
#         print(f"The shape of image is: {arr.shape}")
#         print(arr)

#         return arr

#     except FileNotFoundError:
#         print("Error: File not found.")
#         return None
#     except Exception as e:
#         print(f"Unexpected error: {e}")
#         return None