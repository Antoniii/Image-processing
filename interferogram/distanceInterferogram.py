# conda activate distance
# conda deactivate

"""
Python 3.6.5 [GCC 7.2.0] 
skimage 0.13.1
PIL 5.1.0
numpy 1.14.3
cv2 3.4.1
"""

from skimage import feature, color
from PIL import Image
import numpy as np
import cv2 ###

# can be used COLOR_PARAM = 1
COLOR_PARAM = 255
# minimum distance between pixels
EPS = 3


def sma_filter(y, s=10):
    r = [np.mean(y[i-s:i]) for i in range(s, y.shape[0])]
    return np.array(r)


def calculate(img_name, sigma, filtering=False): # sigma=1
    image = cv2.imread(img_name, 0)

    if filtering: # convolution is used to increase clarity
        image = cv2.filter2D(image, cv2.CV_64F, kernel = np.matrix([-.1,-.1,-.1,-.1, 2 ,-.1,-.1,-.1,-.1]))

    edges = feature.canny(color.rgb2gray(image), sigma=sigma)
    arr = edges.astype('uint8') * 255
    image = Image.fromarray(arr, 'L').convert('1')
    
    image.show()
    #image.save('img1.png')
    
    # if there is one in the line, True, otherwise False
    r = arr.any(axis=1)
    # the indexes of the elements True
    indexes = np.where(r == True)[0]
    # take only the 1st and last, i.e. min and max
    min_y, max_y = indexes[0], indexes[-1]
    #  find the coordinates of all x-owls from which the first line begins
    x_pos = np.array([np.where(arr[index] == COLOR_PARAM)[0][0] for index in range(min_y, max_y)])
    y_pos = np.arange(min_y, max_y)
    # smooth up to 20% of the entire sample
    m_len = int(len(x_pos) * 0.20)
    x_pos = sma_filter(x_pos, s=m_len)
    y_pos = sma_filter(y_pos, s=m_len)
    # find the angle
    res = np.polyfit(x_pos, y_pos, 1)
    angle = np.degrees(np.arctan(res[0])) - 90
    if np.abs(angle) > 90:
        angle %= 90
    print('angle =', round(angle,2))
    image = image.rotate(angle, resample=Image.BILINEAR)
    
    #image.show()

    # find the distance

    r_x, r_y = [], []
    for y in range(image.size[1]):
        for x in range(image.size[0]):
            if image.getpixel((x, y)) == COLOR_PARAM:
                r_x.append(x)
                r_y.append(y)
    max_x, max_y = max(r_x), max(r_y)
    min_x, min_y = min(r_x), min(r_y)
    perc = (max_y - min_y) * 0.15
    cropped = image.crop((min_x, min_y + perc, max_x, max_y - perc))
    points = []
    for y in range(cropped.size[1]):
        data = []
        for x in range(cropped.size[0]):
            if cropped.getpixel((x, y)) == COLOR_PARAM:
                if len(data) > 0 and x - data[-1] <= EPS:
                    data[-1] = x
                else:
                    data.append(x)
        if len(data) >= 4:
            mean = 0
            for a, b in zip(data, data[1:]):
                mean += b - a
            mean /= len(data) - 1
            points.append(mean)
    distance = round(sum(points) / len(points))
    return distance, cropped


if __name__ == '__main__':
    r1 = calculate("test-photo5.jpg", sigma=3.3, filtering=False) 
    # calculate('test\test-photo2.jpg', sigma=3.45, filtering=False)
    # calculate('test\test-photo1.jpg', sigma=4., filtering=True)
    # calculate('test\test-photo3.jpg', sigma=4., filtering=True)
    # calculate('test\test-photo4.jpg', sigma=4., filtering=True)
         
    r1[1].show()
    distance = r1[0]
    print('interference fringe width {} pixels'.format(distance))
