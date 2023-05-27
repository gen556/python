import cv2
import numpy as np


def detect_lanes(image):
    # 灰度化圖像
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 使用高斯模糊進行平滑處理
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # 使用Canny邊緣檢測器檢測邊緣
    edges = cv2.Canny(blur, 50, 150)

    # 使用霍夫直線變換檢測直線
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50,
                            minLineLength=100, maxLineGap=50)

    # 畫出直線
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)

    return image


# 讀取圖像
img = cv2.imread('freeway.jpg')

# 呼叫detect_lanes函數
img2 = detect_lanes(img)

# 顯示結果
cv2.imshow("before", img)
cv2.imshow('Result', img2)
cv2.waitKey(0)
