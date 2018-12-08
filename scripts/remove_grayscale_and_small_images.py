# we can't use grayscale images for training or testing
# this script is to remove grayscale images in the datasets

from datetime import datetime
from PIL import Image
from scipy.misc import imread, imsave, imresize
import os
import random

def is_grey_scale_2(directory, f):
  count = 0
  for filename in os.listdir(directory):
    if filename.endswith('.jpg'):
      path = os.path.join(directory, filename)  
      image = imread(path)
      if len(image.shape) < 3:
        count += 1
#        os.remove(path)
        dest_path = os.path.join(os.path.join(directory, 'grayscale'), filename)
        os.rename(path, dest_path)
        print(path + ", gray scale image is deleted!")
        f.write(path + ", gray scale image is deleted!\n")
      else:
        im = Image.open(path).convert('RGB')
        w,h = im.size
        if w < 180 and h < 180:
          dest_path = os.path.join(os.path.join(directory, 'smallimages'), filename)
          os.rename(path, dest_path)
          continue
        i = 0
        for i in range(10):
          x = random.randint(1, w - 1)
          y = random.randint(1, h - 1)
          r,g,b = im.getpixel((x,y))
          if r != g != b:
            break
          if (i == 9):
            count += 1
#            os.remove(path)
            dest_path = os.path.join(os.path.join(directory, 'grayscale'), filename)
            os.rename(path, dest_path)
            print(path + ", gray scale image is deleted!")
            f.write(path + ", gray scale image is deleted!\n")
  return count

def main():
  f = open(datetime.now().strftime('delete_gray_scale_files_%H_%M_%d_%m_%Y.log'),'w+')
  folder = "datasets/young2old"
  for name in os.listdir(folder): 
    subfolder = os.path.join(folder, 'trainB')
    if os.path.isdir(subfolder):
      print(subfolder)
      f.write("start to delete gray scale images in " + subfolder + ":\n")
      counts = is_grey_scale_2(subfolder, f)
      if counts == 0:
        print("gray scale image not found in " + subfolder)
        f.write("gray scale image not found in " + subfolder)
      print("deleted " + str(counts) + "gray scale images in " + subfolder)
      f.write("deleted " + str(counts) + "gray scale images in " + subfolder + "\n")

if __name__ == '__main__':
  main()
