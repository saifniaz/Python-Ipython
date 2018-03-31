import argparse
import cv2
import numpy as np
from matplotlib import pyplot as plt

def part4(imgfile1, imgfile2, text):


    img1 = cv2.imread(imgfile1, cv2.IMREAD_GRAYSCALE)
    cv2.imshow('Input image1',img1)

    img2 = cv2.imread(imgfile2, cv2.IMREAD_GRAYSCALE)
    cv2.imshow('Input image1',img2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='CSCI 4220U A2.')
    parser.add_argument('imgfile1', help='Image file')
    parser.add_argument('imgfile2', help='Image input')
    parser.add_argument('text', help='Text file')
    args = parser.parse_args()

    imgfile1 = "C:/Users/saif_/Documents/computer_vision/A2/" + args.imgfile1
    imgfile2 = "C:/Users/saif_/Documents/computer_vision/A2/" + args.imgfile2
    text = "C:/Users/saif_/Documents/computer_vision/A2/" + args.text

    part4(imgfile1, imgfile2, text)
