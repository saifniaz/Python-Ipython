import argparse
import cv2
import numpy as np
from matplotlib import pyplot as plt

def filter(img):
    # Complete this method according to the tasks listed in the lab handout.
    x, y = img.shape

    mu = img.mean()
    
    g_img = [[0 for a in range(x)]for b in range(y)]
    for i in range(1, a):
        for j in range(1, b):
            g_img = gaussian2d(mu,img[i][j], 3)

    return g_img

def xder(img):
    ximg = cv2.Sobel(img, -1, 1, 0, ksize=3)
    return ximg

def yder(img):
    yimg = cv2.Sobel(img, -1, 0, 1, ksize=3)
    return yder

def gaussian2d(mu,cov, n):
    var = cov * cov
    shape = (n,n)
    n,m = [(i - 1)/2 for i in shape]
    x,y = np.ogrid[-m:m+1,-n:n+1]
    g = (1/np.sqrt(2*np.pi*var))*np.exp( -(x*x + y*y) / (2*var) )
    return g


def process_img1(imgfile, task):
    print 'Opening ', imgfile
    img = cv2.imread(imgfile, 0)

    # You should implement your functionality in filter function
    if task is 1:
        filtered_img = filter(img)
    elif task is 2:
        filtered_img = xder(img)
    elif task is 3:
        filtered_img = yder(img)
    elif task is 4:
        print ""
    elif task is 5:
        print ""
        

    cv2.imshow('Input image',img)
    cv2.imshow('Filtered image',filtered_img)

    print 'Press any key to proceed'   
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def process_img2(imgfile, task):
    print 'Opening ', imgfile
    img = cv2.imread(imgfile)

    # You should implement your functionality in filter function
    filtered_img = filter(img)

    # You should implement your functionality in filter function

    plt.subplot(121)
    plt.imshow(img)
    plt.title('Input image')
    plt.xticks([]), plt.yticks([])

    plt.subplot(122)
    plt.imshow(filtered_img)
    plt.title('Filtered image')
    plt.xticks([]), plt.yticks([])

    plt.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='CSCI 4220U Lab 2.')
    parser.add_argument('--task', help='task to perform')
    parser.add_argument('imgfile', help='Image file')
    args = parser.parse_args()
    print(args.imgfile)

    imgfile = "C:/Users/saif_/Documents/computer_vision/lab_2/" + args.imgfile
    task = int(args.task)
        

    process_img1(imgfile, task)
