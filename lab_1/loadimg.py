import cv2

img = cv2.imread("C:/Users/saif_/Documents/computer_vision/lab_1/test.jpg")
cv2.imshow('Test',img)
k = cv2.waitKey(0)
if k == ord('q'):
    cv2.destroyAllWindows()
