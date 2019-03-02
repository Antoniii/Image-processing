from PIL import Image, ImageFilter, ImageChops
from numpy import *
from pylab import *

im1 = Image.open('photo-538.png')
im2 = Image.open('photo-539.png')

im = array(Image.open('photo-539.png'))#.convert('1'))
im_negative = 255 - im
#imshow(im_negative)
#show()

#print(im1.size, int(im1.size[0]/4), int(im1.size[1]/4))
#im1.resize((int(im1.size[0]/8), int(im1.size[1]/8)))

#im1.rotate(45).show() 

#im1.filter(ImageFilter.SHARPEN).filter(ImageFilter.DETAIL).show()
#im1.filter(ImageFilter.CONTOUR).show()
#im1.filter(ImageFilter.DETAIL).show()
#im1.filter(ImageFilter.EMBOSS).show()
#im1.filter(ImageFilter.SHARPEN).show()
#im1.filter(ImageFilter.BLUR).show()

#im1.convert('L').show()
#print(im1.getextrema())
#print(im1.filter(ImageFilter.BLUR).getextrema())

imgL = ImageChops.lighter(im1,im2)
imgD = ImageChops.darker(im1,im2)
imgDif = ImageChops.difference(im1,im2)
#print(imgDif.getextrema())

# Y = 0.299*R + 0.587*G + 0.114*B
print('Image Difference Brightness = ',imgDif.convert("L").getextrema()[1]) 

#imgL.show()
imgDif.show()
imgDif.convert("1").show()
#imgDif.convert("L").show()