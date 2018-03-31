import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('lightbox.jpg', 0)
edges = cv.Canny(img,100,200)

yellow = 10
lime = 50
green = 80
l_blue = 110
r_blue = 140
blue = 170
purple = 194
pink = 216
red = 240
orange = 5
y_orange = 250
sun = 245

sobelx = cv.Sobel(img,-1,1,0,ksize=5)
sobely = cv.Sobel(img,-1,0,1,ksize=5)

x, y = edges.shape

for i in range(1, (x-1)):
	for j in range(1, (y-1)):
		if(edges[i][j] > 0):
			Ix = sobelx[i][j]
			Iy = sobely[i][j]
			theta = np.arctan(Iy/Ix)
			theta = theta * (180/np.pi)
			if(theta >= 0.00 and theta < 30.00):
				edges[i][j] = yellow
			elif(theta >= 30.00 and theta < 60.00):
				edges[i][j] = lime
			elif(theta >= 60.00 and theta < 90.00):
				edges[i][j] = green
			elif(theta >= 90.00 and theta < 120.00):
				edges[i][j] = l_blue
			elif(theta >= 120.00 and theta < 150.00):
				edges[i][j] = r_blue
			elif(theta >= 150.00 and theta < 180.00):
				edges[i][j] = blue
			elif(theta >= 180.00 and theta < 210.00):
				edges[i][j] = purple
			elif(theta >= 210.00 and theta < 240.00):
				edges[i][j] = pink
			elif(theta >= 240.00 and theta < 270.00):
				edges[i][j] = red
			elif(theta >= 270.00 and theta < 300.00):
				edges[i][j] = orange
			elif(theta >= 300.00 and theta < 330.00):
				edges[i][j] = y_orange
			elif(theta >= 330.00 and theta < 360.00):
				edges[i][j] = sun
			#print(edges[i][j])


plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges)
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()
