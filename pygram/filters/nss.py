import numpy as np
from PIL import Image, ImageEnhance

def nss(image):
    size     = image.size
    nss      = Image.new('RGBA', size, (243, 106, 188, 77))
    enhancer = ImageEnhance.Contrast(nss)
    enhancer.enhance(1.1)
    enhancer = ImageEnhance.Brightness(nss)
    enhancer.enhance(1.1)
    enhancer = ImageEnhance.Color(nss)
    enhancer.enhance(1.3)

    copy     = image.copy()

    copy.paste(nss, (0,0), nss)

    return copy
