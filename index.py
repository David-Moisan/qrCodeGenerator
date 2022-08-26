image_url = 'https://is1-ssl.mzstatic.com/image/thumb/Purple123/v4/e3/83/b7/e383b75c-51bd-4b81-b146-c872c67dd9ff/AppIcon-1x_U007emarketing-0-7-0-0-85-220.png/1200x600wa.png'

text_url = 'https://extranet.cabinetchaubet.com/bo_ccc/index.php';

from PIL import Image
import requests

image = Image.open(requests.get(image_url, stream=True).raw)
min_width_height = min(image.size)
image = image.crop(((image.size[0] - min_width_height)/2, (image.size[1] - min_width_height)/2, min_width_height, min_width_height))
image.save('image_source.png')

image1 = image.resize((186,186), Image.Resampling.LANCZOS)
image1.save('image_186x186.png')

image2 = image.resize((93, 93), Image.Resampling.LANCZOS)
image2.save('image_93x93.png')

# https://medium.com/geekculture/generate-qr-codes-from-images-using-python-60e669653440 for the tuto
# https://github.com/xyzzy/qrpicture for next step 
