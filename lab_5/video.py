import cv2
import numpy as np
import os
import sys
import csv

temp_list = []

def get_image_files(dirpath):
	filepaths = []

	for root, dirs, files in os.walk(dirpath):
		if root == dirpath:
			for filename in files:
				if os.path.splitext(filename)[1].lower() in ['.jpg', '.jpeg', '.gif', '.png']:
					filepaths.append( os.path.join(root, filename) )
		else:
			continue

	return filepaths

def display_images(filepaths):
	load_file()
	print(temp_list[2])
	c = 0
	for filepath in filepaths:
		img_bgr = cv2.imread(filepath)
		img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
		filter_img(img_rgb, c)
		c = c + 1
		cv2.imshow('Display Window', img_rgb)
		cv2.waitKey(5)

	cv2.destroyAllWindows()

def filter_img(imgfile, C):
	i, j, k, l = temp_list[C].split(",")
	i = int(i)
	j = int(j)
	k = int(k)
	l = int(l)
	cv2.rectangle(imgfile, (i-k,j-k), (i+l, j+l), (0,255,255), 3)


def load_file():
	fname = "Pool_ce1\Pool_ce1_gt.txt"
	with open(fname) as f:
		for line in f:
			temp_list.append(line)

if __name__ == '__main__':
	
	filepaths = get_image_files(sys.argv[1])
	display_images(filepaths)
