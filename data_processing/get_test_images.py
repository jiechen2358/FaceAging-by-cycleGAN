import os
import shutil

RESULT_ROOT_PATH = '/Users/yu/Desktop/cs230_project/results'
RELATIVE_PATH = 'test_latest/images'
DESTINATION_PATH = '/Users/yu/Desktop/cs230_project/images_poster/tmp'

FILES_TO_COPY = [
	'10016074_1987-07-27_2012',
]

FILENAME_SUFFIXES = [
	'_fake_B.png',
	'_real_A.png',
	'_rec_A.png',
]

def getModelName(path):
	return path[len(RESULT_ROOT_PATH ) + 1 : - (len(RELATIVE_PATH) + 1)]


def copyTestImages():
	model_names = [name for name in os.listdir(RESULT_ROOT_PATH)]
	model_paths = [os.path.join(RESULT_ROOT_PATH, name, RELATIVE_PATH) for name in model_names]
	model_paths = [path for path in model_paths if os.path.isdir(path)]
	if not (os.path.isdir(DESTINATION_PATH)):
		os.mkdir(DESTINATION_PATH)
	for model_path in model_paths:
		model_name = getModelName(model_path)
		for filename in FILES_TO_COPY:
			for filename_suffix in FILENAME_SUFFIXES:
				src_path = os.path.join(model_path, filename + filename_suffix)
				if os.path.isfile(src_path):
					dst_path = os.path.join(DESTINATION_PATH, model_name + '_' + filename + filename_suffix)
					shutil.copy(src_path, dst_path)


def main():
	copyTestImages()


if __name__ == '__main__':
    main()