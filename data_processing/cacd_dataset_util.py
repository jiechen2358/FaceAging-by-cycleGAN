#! /usr/bin/env python
# coding: utf-8

from PIL import Image
from resizeimage import resizeimage
import os
import shutil

"""
Utility class to process images downloaded from 
https://drive.google.com/file/d/0B3zF40otoXI3OTR0Y0MtNnVhNFU/

Data source: Cross-Age Celebrity Dataset (CACD)
- http://bcsiriuschen.github.io/CARC/
"""
def group_age(src):
    for file_name in os.listdir(src):
        if file_name.endswith('.jpg'):
            full_file_name = os.path.join(src, file_name)
            if file_name.startswith('1'):
                dest = os.path.join(src, '10')
            elif file_name.startswith('2'):
                dest = os.path.join(src, '20')
            elif file_name.startswith('3'):
                dest = os.path.join(src, '30')
            elif file_name.startswith('4'):
                dest = os.path.join(src, '40')
            elif file_name.startswith('5'):
                dest = os.path.join(src, '50')
            elif file_name.startswith('6'):
                dest = os.path.join(src, '60')
            else:
                dest = os.path.join(src, 'ohter')
            if not os.path.exists(dest):
                os.mkdir(dest)
            shutil.copy(full_file_name, dest)

def resize_image(directory, size):
    """
    :param directory: directory of images to resize
    :param size: for 100x100 image, use [100,100]
    """
    for file_name in os.listdir(directory):
        if file_name.endswith('.jpg'):
            with open(os.path.join(directory, file_name), 'r+b') as f:
                with Image.open(f) as image:
                    cover = resizeimage.resize_cover(image, size)
                    cover.save(os.path.join(directory, 'rs_' + file_name), image.format)

def main():
    src = 'C:\\Training\\DeepLearningGit\\CACD2000'
    group_age(src)

if __name__ == '__main__':
    main()