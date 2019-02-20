import base64
import sys

# Part 1: coder
## python image_to_base64.py helsinki2.jpg

input_image = sys.argv[1]

image = open(input_image, 'rb')
image_read = image.read()
image_64_encode = base64.encodebytes(image_read)

with open('image_encode.txt', 'wb') as f:
    f.write(image_64_encode)
'''


# Part 2: decoder
## python image_to_base64.py .jpg

format_image = sys.argv[1]

time_str = b''
with open('image_encode.txt', 'rb') as f:
    for line in f:
        time_str += line

image_64_decode = base64.decodebytes(time_str)#(image_64_encode) 
image_result = open('image_decode' + format_image, 'wb') # create a writable image and write the decoding result
image_result.write(image_64_decode)
'''