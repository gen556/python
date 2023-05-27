import cv2
import numpy as np

# 讀取影像
img = cv2.imread('osaka.jpg')

# 轉換為灰階影像
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 計算x和y方向的梯度
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

# 取絕對值並轉換為8位灰階影像
sobelx = cv2.convertScaleAbs(sobelx)
sobely = cv2.convertScaleAbs(sobely)

# 結合x和y方向的梯度
sobel = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)

# 顯示結果
cv2.imshow('Input Image', img)
cv2.imshow('Sobel Edge Detection Result', sobel)
cv2.waitKey(0)
cv2.destroyAllWindows()
