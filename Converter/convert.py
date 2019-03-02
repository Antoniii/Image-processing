from PIL import Image
from io import BytesIO
import base64
from os.path import basename, splitext

base64.MAXBINSIZE = -1 # хак: делаем бесконечную длину строки

def convert_image(input, *, output=None, save_jpg=False):
    if output is None:
        output = splitext(basename(input))[0]

    stream = BytesIO()

    img = Image.open(input).convert('RGB')

    img.save(stream, format='jpeg')
    if save_jpg:
        with open(output + '.jpg', 'wb') as f:
            img.save(f, format='jpeg')

    stream.seek(0)

    with open(output + '.txt', 'wb') as f:
        f.write(b'data:image/jpg;base64,')
        base64.encode(stream, f)

if __name__ == '__main__':
    convert_image('from0toF.png', save_jpg=True)
