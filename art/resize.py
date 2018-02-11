# resize.py
"""Script resizes all images in current directory """

import PIL
from PIL import Image

import os

files = []
for element in os.listdir('.'):
    if os.path.isfile(element) and element.endswith('.png'):
        files.append(element)

print "Filenames....."
print files
for pic in files:
    # get sizes of image
    img = Image.open(pic)
    img.save('old-' + pic)
    width, height = img.size
    print "image width %d, height %d" % (width, height)

    newImage = img.resize((int(width * 2), int(height * 2)))
    newImage.save(pic)
