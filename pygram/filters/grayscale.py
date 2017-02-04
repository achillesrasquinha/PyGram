import numpy as np
from PIL import Image

def grayscale(image):
    array = np.array(image)
    r,g,b = array[:,:,0], array[:,:,1], array[:,:,2]

    gray  = 0.2126 * r + 0.7152 * g + 0.0722 * b
    gray  = Image.fromarray(gray)

    return gray
