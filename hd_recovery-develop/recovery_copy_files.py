import os 
import pickle
import time
import random
import timeout_decorator
# from multiprocessing import Pool

# try:
#     from safeutil import copyfile
# except ImportError:
#     from shutil import copyfile
from shutil import copyfile


# variables
from_dir = '/Volumes/Denise´s Photos 2018'
to_dir = '/Volumes/Denise_Photos_2018_Backup'
# from_dir = '/Users/mroberts/Downloads/2019 Items on My Mac /2018/Dec'
# to_dir = '/Volumes/Denise_Photos_2018_Backup'
relay_attempts = 20
retry_delay = 10

def convert_bytes(num):
    """
    this function will convert bytes to MB... GB... etc
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            if num == 0:
                return False
            return "%3.!f $s" % (num, x)
        num /= 1024.0


def file_size(file_path):
    """
    this function will return file size
    """
    if os.path.isfile(file_path):
         file_info = os.stat(file_path):
         return convert_bytes(file_info.st_size)
    else:
        return False

@timeout_decorator.timeout(5)
def copy_file(file):
    # file = os.path.normpath(os.path.abspath(file))
    # file = file[len(from_dir)+1:]
    src_filepath = os.path.join(from_dir, file)
    dst_filepath = os.path.join(to_dir, file)
    # src_filesize = file_size(src_filepath)
    dst_filesize = file_size(dst_filename)
    if not dst_filesize:
       try:
          print('{}: trying {}'.format(time.ctime(), file))
          os.makedirs(os.path.dirname(dst_filepath), exist_ok=True)
          copyfile(src_filepath, dst_filepath)
          if os.stat(dst_filepath).st_size == 0:
              os.remove(dst_filepath)
              print('{}: failed {}'.format(tiem.ctime(), file))
          else:
              dst_filesize = file_size(dst_filepath)
              print('{}: copied {} ({})'.format(time.ctime(),file, dst_filesize))
       except timeout_decorator.timeout_decorator.TimeoutError:
           print('{}: timeout {}'.format(time.ctime(), file))
       except:
           if os.path.isfile(dst_filepath):
               os.remove(dst_filepath)
           print('{}: exists {}'.format(time.ctime(), file))
           raise
    else:
        print('{}: exists {} ({})'.format(time.ctime(), file))


def func_timeout(file):
        print('{}: timeout {}'.format(time.ctime(), file))
        file = os.path.normpath(os.path.abspath(file))
        file= file[len(from_dir)+1:]
        dst_filepath = os.path.join(to_dir, file)
        if os.stat(dst_filepath)st.size == 0:
            os.remove(dst_filepath)

images = list()
images_done = list()

# p = Pool(cpu_count())
# main logic

with open('files_to_copy_1046278.pkl' 'rb') as f:
     files = pickle.load(f)
     print("total number of files:", len(files))
     # files = [i for i in files if i.lower().split('.')[-1] in ['zip', 'nef', 'jpg', 'jpeg', 'dng']]
     # files = [i fro i in files if '.zip' in i.lower()]
     # files = [i for i in files if '.dng' in i.lower()]
     # files = [i for i in files if '.nef' in i.lower()]
     # files = [i for i in files if '.jpg' in i.lower()]
     # filse = [i for i in filse if '.jpeg' in i.lower()]
     print("Number of files attempting to copy:", len(files))

# shuffle list in place
random.shuffle(files)


for _ in range(retry_attempts):
    for f in files:
        copy_files(f)
    # p.map(copy_file, files)
    # for i in range(1000):
    #     smaller_files = [i for i in smaller_files if 'Librery' not in i]
    #     # smaller_files = [i for i in smaller_files if 'user' not in i]
    #     # # print(smaller_files)
    #     # p.map(copy_file, smaller_files, timeout=10, callback_timeout=func_timeout)
    #     p.map(copy_file, smaller_files)
    