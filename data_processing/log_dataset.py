from datetime import datetime
import os

DATASET_PATH = '/Users/yu/Documents/SCPD/CS230/FaceAging-by-cycleGAN/datasets/young2old'
SPECIAL_TAG = 'all'   # 'male' or 'female'

LEFT_DATASET_LOG_PATH = ''
RIGHT_DATASET_LOG_PATH = ''

def dumpFilenamesToLog(collection_data_path, collection_log_path):
	log = open(collection_log_path,'w+')
	for file in os.listdir(collection_data_path):
		log.write(file + "\n")
	log.close()


def generateLogs():
	log_dir_name = datetime.now().strftime('data_log_%H%M_%d%m%Y')
	if SPECIAL_TAG:
		log_dir_name = log_dir_name + '_' + SPECIAL_TAG
	log_path = os.path.join(DATASET_PATH, log_dir_name)
	if not os.path.exists(log_path):
		os.mkdir(log_path)
	for collection_name in ['trainA', 'trainB', 'testA', 'testB']:
		collection_data_path = os.path.join(DATASET_PATH, collection_name)
		collection_log_path = os.path.join(log_path, collection_name + '.log')
		dumpFilenamesToLog(collection_data_path, collection_log_path)


def checkTwoLogFiles(left_path, right_path):
	left_log = open(left_path,'r')
	right_log = open(right_path, 'r')
	left_set = set(left_log.read().splitlines())
	right_set = set(right_log.read().splitlines())
	return left_set & right_set


def compareLogs():
	log_path = os.path.join(DATASET_PATH, '')
	to_compare_log_path = os.path.join(TO_COMPARE_DATASET_PATH, '')
	for collection_name in ['trainA', 'trainB', 'testA', 'testB']:
		left_path = os.path.join(LEFT_DATASET_LOG_PATH, collection_name + '.log')
		rigth_path = os.path.join(RIGHT_DATASET_LOG_PATH, collection_name + '.log')
		diff = checkTwoLogFiles(left_path, rigth_path)


def main():
	generateLogs()


if __name__ == '__main__':
    main()
