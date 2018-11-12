#! /usr/bin/env python
# coding: utf-8

"""
Small util to verify fromat of the input image.
"""

import os
import imghdr

DATA_PATH_FILTERED = '/Users/yu/Desktop/CS230_Data/wiki_filtered/old'

def main():
	count = 0
	for root, dirs, files in os.walk(DATA_PATH_FILTERED, topdown=False):
		for name in files:
			filepath = os.path.join(root, name)
			count += 1
			if imghdr.what(filepath) is not 'jpeg':
				print(filepath)
	print(count)

if __name__ == '__main__':
    main()

