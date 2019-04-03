# conda activate py2ins2exe ## python --version ### 3.7.1
# pip install matplotlib
# conda install pillow
# pip install pyinstaller

# pyinstaller --onedir --onefile --icon=app.ico --name=distance_between_points "C:путь_до_файла\distance-between-points_for-exe.py"

# deactivate

src_name = input("Enter the name of the picture with the extension ")
dst_name = '.'.join(src_name.split('.')[:-1]) + '.png'

COLOR_LINE = input("Bring me the color for line (WHITE, RED, GREEN, BLUE or BLACK) ")

from PIL import Image, ImageDraw
from pylab import imshow, array, sqrt, ginput

img = Image.open(src_name)

im = array(img)
imshow(im)
print('Please click 2 points')
x = ginput(2)
y = [(int(p), int(q)) for p, q in x]
print('You clicked: ', y)

a = [y[0][0], y[0][1], y[1][0], y[1][1]]

clr1 = img.getpixel(y[0])
clr2 = img.getpixel(y[1])
print('Color 1 point {} is'.format((a[0],a[1])), clr1) # color of the first selected pixel
print('Color 2 point {} is'.format((a[2],a[3])), clr2) # color of the second selected pixel

d = int(sqrt((a[0]-a[2])**2+(a[1]-a[3])**2)) # distance between selected pixels

def diff(x,y):
	return list(map(lambda a, b: abs(a-b), x, y))

delta_color = diff(clr1,clr2) # color difference between pixels to control selection

print('The distance between the points = {} pixels\n'.format(d), 
	'Point color difference =', delta_color)

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

draw = ImageDraw.Draw(img)
draw.line([(a[0],a[1]),(a[2],a[3])], fill=COLOR_LINE, width=3)
img.save(dst_name, dpi=(300,300))
img.show()
input("Press ENTER key to close the window")