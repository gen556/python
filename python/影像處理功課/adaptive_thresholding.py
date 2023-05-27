import numpy as np
import cv2
import math

img = cv2.imread("osaka.jpg", 0)  # 讀取
thresh, img1 = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)
img2 = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 0)
img3 = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 0)


cv2.imshow("Original Image", img)  # 原圖
cv2.imshow("Gobal Threshoulding", img1)  # Circle後
cv2.imshow("Adaptive Threshoulding(Mean)", img2)  # Circle後
cv2.imshow("Adaptive Threshoulding(Gaussian)", img3)  # Circle後
cv2.waitKey(0)
