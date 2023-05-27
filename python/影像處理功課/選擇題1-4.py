import cv2
import numpy as np

# 讀取影像
img = cv2.imread('osaka.jpg')

# 轉換為灰階影像
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 定義Robinson算子
robinson_0 = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
robinson_1 = np.array([[0, 1, 2], [-1, 0, 1], [-2, -1, 0]])
robinson_2 = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
robinson_3 = np.array([[2, 1, 0], [1, 0, -1], [0, -1, -2]])
robinson_4 = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])
robinson_5 = np.array([[0, -1, -2], [1, 0, -1], [2, 1, 0]])

# 執行Robinson算子
g0 = cv2.filter2D(gray, -1, robinson_0)
g1 = cv2.filter2D(gray, -1, robinson_1)
g2 = cv2.filter2D(gray, -1, robinson_2)
g3 = cv2.filter2D(gray, -1, robinson_3)
g4 = cv2.filter2D(gray, -1, robinson_4)
g5 = cv2.filter2D(gray, -1, robinson_5)

edge = np.max(np.stack([g0, g1, g2, g3, g4, g5], axis=-1), axis=-1)

# 顯示結果
cv2.imshow('Input Image', img)
cv2.imshow('Edge Detection Result', edge.astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()
