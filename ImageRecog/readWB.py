import pytesseract

from PIL import Image, ImageEnhance, ImageFilter

im = Image.open('testext.png')
im = im.filter(ImageFilter.MedianFilter())
enhancer = ImageEnhance.Contrast(im)
im = enhancer.enhance(2)
im = im.convert('1')
im.save('testext2.jpg')

text = pytesseract.image_to_string(Image.open('testext2.jpg'))
print(text)
