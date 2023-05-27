import numpy as np
import cv2

img1 = cv2.imread("1.jpg", -1)
img2 = 255-img1
cv2.imshow("1", img1)
cv2.imshow("2", img2)
cv2.waitKey(0)
