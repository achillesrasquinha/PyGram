import numpy as np
from PIL import Image

def grayscale(image):
    rgb   = np.asarray(image)
    r,g,b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray  = 0.2126 * r + 0.7152 * g + 0.0722 * b
    image = Image.fromarray(gray)


    return image
