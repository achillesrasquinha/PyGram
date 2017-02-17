from PIL import Image, ImageEnhance

def clarendon(image):
    size      = image.size
    clarendon = Image.new('RGBA', size, (127, 187, 227, 51))
    enhancer  = ImageEnhance.Contrast(clarendon)
    enhancer.enhance(1.20)
    enhancer  = ImageEnhance.Color(clarendon)
    enhancer.enhance(1.35)

    copy      = image.copy()

    copy.paste(clarendon, (0, 0), clarendon)

    return copy
