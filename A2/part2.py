import argparse
import cv2
import numpy as np
from numpy.linalg import inv
from matplotlib import pyplot as plt

def wrap(imgfile, A):
    print("Opening", imgfile)

    img = cv2.imread(imgfile, cv2.IMREAD_GRAYSCALE)
    cv2.imshow('Input image',img)
    #A = np.array([[290, 0],[290, 460],[0, 460],[0, 0]])
    B = np.array([[160, 0],[290, 330], [460, 190], [0, 200]])

    P = np.zeros((9, 9))
    P[8, 8] = 1

    #print(P)
    cont = 0
    P_c = 0


    while(cont < 4):
        if(P_c == 8):
            break
        p = A[cont]
        q = B[cont]
        m1 = np.array([-p[0], -p[1], -1, 0, 0, 0, (p[0]*q[0]), (p[1]*q[0]), q[0]])
        #print(p)
        P[P_c] = m1
        P_c = P_c + 1
        m2 = np.array([0, 0, 0, -p[0], -p[1], -1, (p[0]*q[1]), (p[1]*q[1]), q[1]])
        #print(q)
        P[P_c] = m2
        P_c = P_c + 1
        cont = cont + 1

    #print(P)

    zero = np.zeros((9, 1))
    zero[8, 0] = 1

    H = np.dot(inv(P), zero)

    H = H.reshape(3, 3)

    print(H)

    x, y= img.shape
    print(x, y)

    

    #h, status = cv2.findHomography(A, B)
    #print(h)

    wrp = np.zeros((x, y), np.uint8)
    
    for v in range(1, (y-1)):
        for u in range(1, (x-1)):            
            temp = np.dot(H, [u, v, 1])
            xP = abs(int(temp.item(0)))%300
            yP = abs(int(temp.item(1)))%468
            #print(xP, yP)
            wrp[xP][yP] = img[u, v]


    cv2.imshow('Warpped image', wrp)

    #plt.imshow(wrp, 'gray')

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='CSCI 4220U A2.')
    parser.add_argument('imgfile', help='Image file')
    parser.add_argument('x0y0', help='Image input')
    parser.add_argument('x1y0', help='Image input')
    parser.add_argument('x0y1', help='Image input')
    parser.add_argument('x1y1', help='Image input')
    args = parser.parse_args()

    imgfile = "C:/Users/saif_/Documents/computer_vision/A2/" + args.imgfile

    pt1 = args.x0y0
    pt2 = args.x1y0
    pt3 = args.x0y1
    pt4 = args.x1y1

    l1 = pt1.split(" ")
    l2 = pt2.split(" ")
    l3 = pt3.split(" ")
    l4 = pt4.split(" ")

    A = np.array([[int(l1[0]), int(l1[1])], [int(l2[0]), int(l2[1])],
        [int(l3[0]), int(l3[1])], [int(l4[0]), int(l4[1])]])

    wrap(imgfile, A)
