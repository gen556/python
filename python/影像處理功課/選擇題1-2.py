import cv2
import numpy as np

# 讀取影像
img = cv2.imread('osaka.jpg')

# 轉換為灰階影像
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 定義Prewitt算子
prewitt_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
prewitt_y = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])

# 執行Prewitt算子
gx = cv2.filter2D(gray, -1, prewitt_x)
gy = cv2.filter2D(gray, -1, prewitt_y)
edge = np.sqrt(gx ** 2 + gy ** 2)

# 顯示結果
cv2.imshow('Input Image', img)
cv2.imshow('Edge Detection Result', edge.astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()
