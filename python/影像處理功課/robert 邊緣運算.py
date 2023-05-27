import cv2
import numpy as np

# 讀取影像
img = cv2.imread('osaka.jpg', cv2.IMREAD_GRAYSCALE)

# 定義Robert梯度運算子的兩個卷積核
roberts_x = np.array([[-1, 0], [0, 1]], dtype=np.float32)
roberts_y = np.array([[0, -1], [1, 0]], dtype=np.float32)

# 對影像進行卷積運算
gx = cv2.filter2D(img, -1, roberts_x)
gy = cv2.filter2D(img, -1, roberts_y)

# 計算邊緣強度
magnitude = np.sqrt(np.square(np.abs(gx)) + np.square(np.abs(gy)))

# 顯示結果
cv2.imshow('Input Image', img)
cv2.imshow('Gradient X', gx)
cv2.imshow('Gradient Y', gy)
cv2.imshow('Magnitude', magnitude)
cv2.waitKey(0)
