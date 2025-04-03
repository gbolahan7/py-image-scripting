import sys
import os
from PIL import Image

# grab first & second argument [ python3 JPGtoPNGconverter.py images/ new/]
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# print(image_folder, output_folder)

# check if the new folder ( this is where the converted image will be stored) is created and if not, create it 
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

#next, loop throught the images folder
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
# convert to PNG
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('done!')
#save to new folder