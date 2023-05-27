import numpy as np
import cv2


img = cv2.imread("osaka.jpg", -1)
img2 = cv2.Canny(img, 15, 200)
cv2.imshow("before", img)
cv2.imshow("after", img2)
cv2.waitKey(0)
