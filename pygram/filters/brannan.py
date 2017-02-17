from PIL import Image, ImageEnhance

from pygram.filters import sepia

def brannan(image):
    size     = image.size
    brannan  = Image.new('RGBA', size, (161, 44, 199, 79))
    enhancer = ImageEnhance.Contrast(brannan)
    enhancer.enhance(1.4)

    copy     = image.copy()
    copy     = sepia(image)

    copy.paste(brannan, (0, 0), brannan)

    return copy
