from PIL import Image
from resizeimage import resizeimage
import os
import shutil
import random

ALL_IMAGES_PATH = '/home/yu/Downloads/CACD2000'
PROCESS_PATH = '/home/yu/Development/FaceAging-by-cycleGAN/datasets/young2old_large_3'


def groupAge(src):
    for file_name in os.listdir(src):
        if file_name.endswith('.jpg'):
            full_file_name = os.path.join(src, file_name)
            if file_name.startswith('0'):
                dest = os.path.join(src, '00')
            if file_name.startswith('1'):
                dest = os.path.join(src, '10')
            elif file_name.startswith('2'):
                dest = os.path.join(src, '20')
            elif file_name.startswith('3'):
                dest = os.path.join(src, '30')
            elif file_name.startswith('4'):
                dest = os.path.join(src, '40')
            elif file_name.startswith('5'):
                dest = os.path.join(src, '50+')
            elif file_name.startswith('6'):
                dest = os.path.join(src, '50+')
            else:
                dest = os.path.join(src, '50+')
            if not os.path.exists(dest):
                os.mkdir(dest)
            shutil.move(full_file_name, dest)


def resizeImage(d, d_out, size):
    for file_name in os.listdir(d):
        if file_name.endswith('.jpg'):
            with open(os.path.join(d, file_name), 'r+b') as f:
                with Image.open(f) as image:
                    cover = resizeimage.resize_cover(image, size)
                    cover.save(os.path.join(d_out, 's_' + file_name), image.format)


def randomChooseFile(train_raw_dst, train_out_dst, test_raw_dst, test_out_dst, src, sample_size):
    test_count = int(round(sample_size / 10))
    train_count = sample_size - test_count

    for i in range(train_count):
        candidate = random.choice(os.listdir(src))
        full_path = os.path.join(src, candidate)
        shutil.move(full_path, train_out_dst)
    # resizeImage(train_raw_dst, train_out_dst, [200, 200])

    for i in range(test_count):
        candidate = random.choice(os.listdir(src))
        full_path = os.path.join(src, candidate)
        shutil.move(full_path, test_out_dst)
    # resizeImage(test_raw_dst, test_out_dst, [200, 200])


def parseFilename(filename):
    parts = filename.split('_')
    age = int(parts[0])
    name = '_'.join(parts[1:-1])
    return age, name


def getGroupNameDifference(ageGroupA, ageGroupB):
    srcA = os.path.join(ALL_IMAGES_PATH, ageGroupA)
    srcB = os.path.join(ALL_IMAGES_PATH, ageGroupB)
    peopleA = set()
    peopleB = set()
    for file in os.listdir(srcA):
        age, name = parseFilename(file)
        peopleA.add(name)
    for file in os.listdir(srcB):
        age, name = parseFilename(file)
        peopleB.add(name)
    print(peopleA & peopleB)


def getImages():
    srcA = os.path.join(ALL_IMAGES_PATH, '20')
    srcB = os.path.join(ALL_IMAGES_PATH, '50+')

    trainA_raw = os.path.join(PROCESS_PATH, 'trainA_raw')
    trainA = os.path.join(PROCESS_PATH, 'trainA')
    os.mkdir(trainA_raw)
    os.mkdir(trainA)
    testA_raw = os.path.join(PROCESS_PATH, 'testA_raw')
    testA = os.path.join(PROCESS_PATH, 'testA')
    os.mkdir(testA_raw)
    os.mkdir(testA)
    randomChooseFile(trainA_raw, trainA, testA_raw, testA, srcA, 2500)

    trainB_raw = os.path.join(PROCESS_PATH, 'trainB_raw')
    trainB = os.path.join(PROCESS_PATH, 'trainB')
    os.mkdir(trainB_raw)
    os.mkdir(trainB)
    testB_raw = os.path.join(PROCESS_PATH, 'testB_raw')
    testB = os.path.join(PROCESS_PATH, 'testB')
    os.mkdir(testB_raw)
    os.mkdir(testB)
    randomChooseFile(trainB_raw, trainB, testB_raw, testB, srcB, 2500)


def main():
    # groupAge(ALL_IMAGES_PATH)
    # getGroupNameDifference('20', '50+')
    # getImages()


if __name__ == '__main__':
    main()
