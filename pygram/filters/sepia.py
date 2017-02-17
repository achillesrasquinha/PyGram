import numpy as np
from PIL import Image

def sepia(image):
    arr        = np.copy(image)
    r,g,b      = arr[:,:,0], arr[:,:,1], arr[:,:,2]

    arr[:,:,0] = np.minimum(r * 0.393 + g * 0.769 + b * 0.189, 255)
    arr[:,:,1] = np.minimum(r * 0.349 + g * 0.686 + b * 0.168, 255)
    arr[:,:,2] = np.minimum(r * 0.272 + g * 0.534 + b * 0.131, 255)

    copy       = Image.fromarray(arr)

    return copy
