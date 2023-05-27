import cv2
import numpy as np

# 讀取影像
img = cv2.imread('osaka.jpg')

# 轉換為灰階影像
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 定義Kirsch算子
kirsch_0 = np.array([[-3, -3, 5], [-3, 0, 5], [-3, -3, 5]])
kirsch_1 = np.array([[-3, 5, 5], [-3, 0, 5], [-3, -3, -3]])
kirsch_2 = np.array([[5, 5, 5], [-3, 0, -3], [-3, -3, -3]])
kirsch_3 = np.array([[5, 5, -3], [5, 0, -3], [-3, -3, -3]])
kirsch_4 = np.array([[5, -3, -3], [5, 0, -3], [5, -3, -3]])
kirsch_5 = np.array([[-3, -3, -3], [5, 0, -3], [5, 5, -3]])
kirsch_6 = np.array([[-3, -3, -3], [-3, 0, -3], [5, 5, 5]])
kirsch_7 = np.array([[-3, -3, -3], [-3, 0, 5], [-3, 5, 5]])

# 執行Kirsch算子
g0 = cv2.filter2D(gray, -1, kirsch_0)
g1 = cv2.filter2D(gray, -1, kirsch_1)
g2 = cv2.filter2D(gray, -1, kirsch_2)
g3 = cv2.filter2D(gray, -1, kirsch_3)
g4 = cv2.filter2D(gray, -1, kirsch_4)
g5 = cv2.filter2D(gray, -1, kirsch_5)
g6 = cv2.filter2D(gray, -1, kirsch_6)
g7 = cv2.filter2D(gray, -1, kirsch_7)

edge = np.max(np.stack([g0, g1, g2, g3, g4, g5, g6, g7], axis=-1), axis=-1)

# 顯示結果
cv2.imshow('Input Image', img)
cv2.imshow('Edge Detection Result', edge.astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()
