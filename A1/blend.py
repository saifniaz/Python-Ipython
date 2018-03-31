import argparse
import cv2
import numpy as np
import time
from matplotlib import pyplot as plt

def blend(imgFile1, imgFile2, alpha):

    beta = 1.0 - alpha

    img1 = cv2.imread(imgFile1)
    img2 = cv2.imread(imgFile2)

    b_img = cv2.addWeighted(img1,alpha,img2,beta,0)
    
    cv2.imshow('Blended image',b_img)

    print "press any key to quit"
    cv2.waitKey(0)
    cv2.destroyAllWindows()



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='CSCI 4220U Lab 2.')
    parser.add_argument('--use-plotlib', action='store_true', help='If specified uses matplotlib for displaying images.')
    parser.add_argument('alpha', help='float')
    parser.add_argument('imgfile1', help='Image file')
    parser.add_argument('imgfile2', help='Image file')
    args = parser.parse_args()

    alpha = float(args.alpha)

    i1 = "C:/Users/saif_/Documents/computer_vision/A1/" + args.imgfile1
    i2 = "C:/Users/saif_/Documents/computer_vision/A1/" + args.imgfile2

    blend(i1, i2, alpha)
