from PIL import Image, ImageFilter
import os 

image1= Image.open('1.jpeg')
image1.rotate(90).save('1_mod.jpeg')
image1.convert(mode='L').save('1_mod_.jpeg')
image1.filter(ImageFilter.GaussianBlur()).save('1_mod_blur.jpeg')
image1.filter(ImageFilter.GaussianBlur(15)).save('1_mod_blur_15.jpeg')