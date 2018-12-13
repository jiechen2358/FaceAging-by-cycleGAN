import os
import shutil

###### CHANGE TWO LINES BELOW TO YOUR DATA PATH AND OUTPUT PATH ######

RESULT_ROOT_PATH = '/Users/yu/Desktop/cs230_project/results'
DESTINATION_PATH = '/Users/yu/Desktop/cs230_project/images_poster/old2young'

######################################################################

###### CHANGE SECTIONS BELOW TO MATCH YOUR DESIRED OUTPUT ######

# YOUNG_TO_OLD
# FILES_TO_COPY = [
# 	'10016074_1987-07-27_2012',
# 	'1030991_1987-09-07_2009',
# 	'1007928_1986-03-09_2009',
# 	'10093585_1989-07-21_2011',
# 	'10241990_1984-11-28_2007',
# 	'10485669_1988-06-11_2014',
# 	'10486529_1986-03-06_2011',
# 	'13016000_1987-01-20_2009',
# 	'13033930_1981-08-01_2007',
# 	'1339248_1989-10-01_2011',
# 	'32613755_1987-09-27_2013',
# 	'32613755_1987-09-27_2013',
# 	'1004429_1981-02-13_2007',
# 	'1010162_1982-01-09_2009',
# 	'10268856_1984-03-01_2013',
# 	'10297431_1984-06-24_2012',
# 	'10592068_1988-05-18_2012',
# 	'5222023_1983-09-29_2008',
# 	'12253254_1987-06-21_2012',
# ]

# OLD_TO_YOUNG
FILES_TO_COPY = [
	'10080646_1986-08-08_2014',
	'10184590_1979-06-16_2006',
	'1020882_1985-12-03_2009',
	'1006407_1980-07-07_2005',
	'10075415_1988-01-11_2010',
	'10323445_1985-06-06_2007',
	'10573756_1981-09-22_2010',
	'1066075_1981-07-08_2005',
	'10953971_1986-08-29_2015',
	'10974219_1962-05-21_2014',
	'13001672_1975-02-27_2000',
	'1303125_1982-02-25_2009',
	'32613755_1987-09-27_2013',
	'1004429_1981-02-13_2007',
	'1024100_1982-06-07_2011',
	'10390893_1987-11-22_2008',
	'1061555_1981-03-12_2009',
	'5230665_1985-05-22_2006',
	'12253254_1987-06-21_2012',
]

################################################################

### CHANGE SECTION BELOW TO SELECT THE HALF OF DATA GENEARTED ###

FILENAME_SUFFIXES = [
	# '_fake_B',  # YOUNG_TO_OLD
	# '_real_A',  # YOUNG_TO_OLD
	'_fake_A',  # OLD_TO_YOUNG
	'_real_B',  # OLD_TO_YOUNG
]

#################################################################

RELATIVE_PATH = 'test_latest/images'
FILETYPE = '.png'


def getModelName(path):
	return path[len(RESULT_ROOT_PATH ) + 1 : - (len(RELATIVE_PATH) + 1)]


def copyTestImages():
	model_names = [name for name in os.listdir(RESULT_ROOT_PATH)]
	model_paths = [os.path.join(RESULT_ROOT_PATH, name, RELATIVE_PATH) for name in model_names]
	model_paths = [path for path in model_paths if os.path.isdir(path)]
	if not (os.path.isdir(DESTINATION_PATH)):
		os.mkdir(DESTINATION_PATH)
	for filename in FILES_TO_COPY:
		# Only copy 1 'REAL' image
		real_filename_suffix = FILENAME_SUFFIXES[1]
		src_path = os.path.join(model_paths[0], filename + real_filename_suffix + FILETYPE)
		if os.path.isfile(src_path):
			dst_path = os.path.join(DESTINATION_PATH,  filename + real_filename_suffix + '_' + getModelName(model_paths[0]) + FILETYPE)
			shutil.copy(src_path, dst_path)
		# Copy all 'FAKE' image
		fake_filename_suffix = FILENAME_SUFFIXES[0]
		for model_path in model_paths:
			model_name = getModelName(model_path)
			src_path = os.path.join(model_path, filename + fake_filename_suffix + FILETYPE)
			if os.path.isfile(src_path):
				dst_path = os.path.join(DESTINATION_PATH,  filename + fake_filename_suffix + '_' + model_name + FILETYPE)
				shutil.copy(src_path, dst_path)


def main():
	copyTestImages()


if __name__ == '__main__':
    main()