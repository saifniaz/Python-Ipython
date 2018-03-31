import argparse
import cv2
import numpy as np
from numpy.linalg import inv
from matplotlib import pyplot as plt

ix,iy = -1,-1
c = 0
A = []
# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy,c
    global A
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),1,(0,0,0),-1)
        ix,iy = x,y
        A.append([ix, iy])
        c = c + 1

def Warp(A, w, h):

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
    print(img.shape)

    

    #h, status = cv2.findHomography(A, B)
    #print(h)

    wrp = np.zeros((w, h), np.uint8)
    
    for v in range(1, (y-1)):
        for u in range(1, (x-1)):            
            temp = np.dot(H, [u, v, 1])
            xP = abs(int(temp.item(0)))
            yP = abs(int(temp.item(1)))
            #print(xP, yP)
            wrp[xP][yP] = img[u, v]


    return wrp


def part3(imgfile, w, h):
	global img
	img = cv2.imread(imgfile, cv2.IMREAD_GRAYSCALE)
	cv2.namedWindow('image')
	cv2.setMouseCallback('image',draw_circle)

	while(1):
	    cv2.imshow('image',img)
	    k = cv2.waitKey(20) & 0xFF
	    if k == ord('a'):
	    	print(ix,iy)
	    if c == 4:
	        break

	img_w = Warp(A, w, h)

	cv2.imshow('Warpped image', img_w)

	cv2.waitKey(0)
	cv2.destroyAllWindows()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='CSCI 4220U A2.')
    parser.add_argument('imgfile', help='Image file')
    parser.add_argument('w', help='Image input')
    parser.add_argument('h', help='Image input')
    args = parser.parse_args()

    imgfile = "C:/Users/saif_/Documents/computer_vision/A2/" + args.imgfile

    w = int(args.w)
    h = int(args.h)

    part3(imgfile, w, h)