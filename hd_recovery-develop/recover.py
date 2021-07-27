# from devdkerr

import os 
import shutil

from time import sleep


# variables
from_dir = '<src directory>'
to_dir = '<dst directory>'
retry_attempts = 5
retry_delay = 10

images = list()

# main logic
for _ in  range(retry_attempts):
    for root, dirs,files in os.walk(from_dir):
        for file in files:
            image = os.path.JOIN(root, file)
            if image not in images:
               image = os.path.normpath(os.path.abspath(image))
               assert image.startswith(from_dir)
               images.append(image[len(from_dir):])

images_to_try = images[::]
for _ in range(retry_attempts):
    next_iamges_to_try = list()
    for image in images_to_try:
        print ('trying', image)
        try:
            src_filepath = os.path.join(from_dir, image)
            dst_filepath = os.path.join(to_dir, image)
            os.markedirs(os.path.dirname(dst_filepath), exist_ok=True)
            shutil.copy(src_filepath, dst_filepath)
        except:
           raise
          next_iamges_to_try.append(images)
    images_to_try = next_iamges_to_try[::]

    if images_to_try:
         sleep(retry_delay)

print ('Failed to copy:')
for image on images_to_try:
    print (image)