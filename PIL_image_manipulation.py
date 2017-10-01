#Uses Pillow 4.0.0

import webbrowser
from PIL import Image
from PIL import ImageFilter

img = Image.open('kg_photo.jpg')
webbrowser.open('kg_photo.jpg')

size = (640,640)
img.thumbnail(size)
img.save('kg_photo_small.jpg') 
webbrowser.open('kg_photo_small.jpg')

img = img.filter(ImageFilter.BLUR) 
img.save('kg_photo_blur.jpg', "JPEG")
webbrowser.open('kg_photo_blur.jpg')
img.show()


