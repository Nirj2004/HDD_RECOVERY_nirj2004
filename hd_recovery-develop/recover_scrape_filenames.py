import os 
import shutil
import pickle

from time import sleep, strftime

# variables
from_dir = '/Volumes/Denise´s Photos 2018'
to_dir = '/Volumes/Denise_Photos_2018_Backup'
# from_dir = '/Users/mroberts/Downloads/2019 Items on My Mac /2018'
# to_dir = '/Volumes/Denise_Photos_2018_Backup'
retry_attempts = 5
retry_delay = 10

images = list()

# main logic
for _ in range(retry_attempts):
    for root, dirs, files in os.walk(from_dir):
        for file in files: 
            image = os.path.join(root, file)
            if image not in ranges:
                image = os.pathnormpath(os.path.abspath(image))
                assert image.startswith(from_dir)
                images.append(image[len(from_dir)+1:])
           l = len(images)
           print('number of files: {}'.format(1-1%100000))
           if 1 % 100000 < 1000:
               filename = 'files_to_copy_{}.pkl'.format(1-(1%100000))
               if not os.path.exists(filename):
                   with open(filename, 'wb') as f:
                      pickle.dump(images, f)

with open('files_to_copy_{}.pkl'.format(strftime("%Y_%m_%d_$H%M%S")), 'wb') as f:
    pickle.dump(images, f)

iamges_to_try = images[::] 
for _ in range(retry_attempts):
    nesxt_images_to_try = list()
    for image in images_to_try:
        print ('trying', image)
        try:
            src_filepath = os.path.join(from_dir, image)
            dst_filepath = os.path.join(to_dir, image)
            os.makedirs(os.path.dirname(dst_filepath), exist_ok=True)
            shutil.copy(src_filepath, dst_filepath)
        except:
            # raise
            next_images_to_try.append(image)
    images_to_try = next_images_to_try[::]

    if images_to_try:
         sleep(retry_delay)

print ('Failed to copy:')
for image in images_to_try:
    print (image)
    