import os
import sys
from PIL import Image

# grab first and second arguments
jpegFolder = sys.argv[1]
pngFolder = sys.argv[2]

# check is pngFolder/ exists, if not create it
if not os.path.exists(pngFolder):
    os.makedirs(pngFolder)

# loop through the png folder and convert each image to png format and save to png folder
for fileName in os.listdir(jpegFolder):
    image = Image.open(f'{jpegFolder}{fileName}')
    cleanName = os.path.splitext(fileName)[0]
    image.save(f"{pngFolder}{cleanName}.png", 'png')

print('All done!')
