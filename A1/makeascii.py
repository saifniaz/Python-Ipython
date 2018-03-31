
import argparse
import cv2
import numpy as np
import time
from matplotlib import pyplot as plt


def makeascii(width,imgfile, outFile):
    thefile = outFile
    
    print "Opening", imgfile

    img = cv2.imread(imgfile, 0)

    y, x = img.shape
    print img.shape

    new = [0 for a in range(y)]

    for i in range(y):
        temp = ''
        for j in range(width*2):
            temp +=(chr((img[j, i] % 15) + 32))
        new[i] = temp


    file = open(thefile, 'w')
    for items in new:
        file.write("%s\n" % items)
    file.close()
                

    cv2.imshow('Input image',img)
    #cv2.imwrite('output.txt', new)
    #cv2.imshow('Laplacian image',lap)
      
    print 'Press any key to proceed'   
    cv2.waitKey(0)
    cv2.destroyAllWindows()



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='CSCI 4220U Lab 2.')
    parser.add_argument('--width', help='Get width')
    parser.add_argument('imgfile', help='Image file')
    parser.add_argument('outFile', help='Output file')
    args = parser.parse_args()

    imgFile = "C:/Users/saif_/Documents/computer_vision/A1/" + args.imgfile
    outFile = args.outFile
    width = int(args.width)

    makeascii(width, imgFile, outFile)
