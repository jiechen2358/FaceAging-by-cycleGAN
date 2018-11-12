
#! /usr/bin/env python
# coding: utf-8

"""
Filter out desired training images and copy them into respective
directories.
"""

import os
import pandas as pd

from collections import defaultdict
from pprint import pprint
from shutil import copy2

# DATA_PATH = '/Users/yu/Dropbox/CS230_Project/Data_Processing/wiki.pkl'
MEATADATA_PATH = '/Users/yu/Dropbox/CS230_Project/Data_Processing/wiki.pkl'
DATA_PATH = '/Users/yu/Desktop/CS230_Data/wiki_crop'
DATA_PATH_FILTERED = '/Users/yu/Desktop/CS230_Data/wiki_filtered'

MINIMUM_IMAGE_SIZE = 2 * 1024  # 2KB
MINIMUM_FACE_SCORE_OLD = 1
MINIMUM_FACE_SCORE_YOUNG = 3
ANALYZE = False

def getGenderString(gender):
	return 'male' if gender == 1.0 else 'female'

def checkValidImage(path_to_image):
	return os.path.isfile(path_to_image) and os.path.getsize(path_to_image) > MINIMUM_IMAGE_SIZE

def checkValidAge(age):
	return age > 0 and age < 100

def getBucketKey(age, increment):
	key = ''
	for i in range(0, 100, increment):
		if age in range(i, i + increment):
			key = str(i) + '_' + str(i + increment - 1)
	return key

def addToBucket5(age, gender, buckets):
	age_key = getBucketKey(age, 5)
	key = gender + '_' + age_key
	buckets[key] += 1

def getBaseFilename(filename):
	return filename.split('/')[-1]

def main():
	metadata = pd.read_pickle(MEATADATA_PATH)

	if ANALYZE:
		columns = list(metadata.columns.values)
		for column in columns:
			print('Column ' + column + ' has ' + str(len(metadata[column])) + ' entries.')

	if ANALYZE:
		age_buckets_5 = defaultdict(int)

	if ANALYZE:
		all_20_30_count = 0
		filtered_20_30_count = 0
		all_50_60_count = 0
		filtered_50_60_count = 0

	for i in range(len(metadata['photo_taken_age'])):

		# need some validation
		age = metadata['photo_taken_age'][i]
		full_path = os.path.join(DATA_PATH, metadata['full_path'][i])
		if not checkValidAge(age) or not checkValidImage(full_path):
			continue

		gender = getGenderString(metadata['gender'][i])

		if ANALYZE:
			addToBucket5(age, gender, age_buckets_5)  

		if gender == 'male':
			if age >= 20 and age < 30:
				if ANALYZE:
					all_20_30_count += 1
				if metadata['face_score'][i] > MINIMUM_FACE_SCORE_YOUNG:
					if ANALYZE:
						filtered_20_30_count += 1
					copy2(full_path, os.path.join(DATA_PATH_FILTERED, 'young', getBaseFilename(metadata['full_path'][i])))
			elif age >=50 and age < 60:
				if ANALYZE:
					all_50_60_count += 1
				if metadata['face_score'][i] > MINIMUM_FACE_SCORE_OLD:
					if ANALYZE:
						filtered_50_60_count += 1
					copy2(full_path, os.path.join(DATA_PATH_FILTERED, 'old', getBaseFilename(metadata['full_path'][i])))

	if ANALYZE:
		print('Images with age breakdown: ')
		pprint(age_buckets_5)
		print('Images betwee 20 and 30 totals: ' + str(all_20_30_count))
		print('Images betwee 20 and 30 filters: ' + str(filtered_20_30_count))
		print('Images betwee 50 and 60 totals: ' + str(all_50_60_count))
		print('Images betwee 50 and 60 filters: ' + str(filtered_50_60_count))

if __name__ == '__main__':
    main()