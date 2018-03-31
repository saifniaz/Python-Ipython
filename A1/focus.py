import argparse
import cv2
import numpy as np
import time
from matplotlib import pyplot as plt


def focus(imgfile):
    print "Opening", imgfile

    img = cv2.imread(imgfile)
    cv2.imshow('Input image',img)

    start = int(round(time.time()* 1000))

    lap = cv2.Laplacian(img,cv2.CV_64F)

    x, y, z = img.shape

    #for i in range(x):
    #    for j in range(y):
    #        for k in range(z):
    #            if(lap[i, j, k] < 0):
    #                print lap[i,j,k]

                    
    lap = cv2.Laplacian(img,-1)

    end = int(round(time.time()* 1000))

    cv2.imshow('Input image',img)
    cv2.imshow('Laplacian image',lap)

    temp = end - start
    print 'Focus analysis took', temp, "ms"
    print 'Press any key to quit'   
    cv2.waitKey(0)
    cv2.destroyAllWindows()



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='CSCI 4220U Lab 2.')
    parser.add_argument('imgfile', help='Image file')
    args = parser.parse_args()

    imgfile = "C:/Users/saif_/Documents/computer_vision/A1/" + args.imgfile

    focus(imgfile)
