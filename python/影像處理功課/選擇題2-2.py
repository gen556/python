import numpy as np
import cv2
import math

img1 = cv2.imread("osaka.jpg", -1)  # 讀取
if img1 is None:  # 檢查讀取
    print("Error: Failed to read image file")
else:
    img2 = img1.copy()  # 複製圖1
    gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)  # 灰階化
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1,
                               150, 200, 50, minRadius=120, maxRadius=200)  # 執行霍夫圓檢測
    if circles is not None and circles[0][0].ndim == 1:  # 檢查是否檢測到圓形
        circles = np.uint16(np.around(circles))  # 四捨五入到最接近的整數
        for i in circles[0, :]:
            if i is not None:
                cv2.circle(img2, (i[0], i[1]), i[2], (0, 255, 0), 2)  # 繪製圓
                cv2.circle(img2, (i[0], i[1]), 2, (0, 0, 255), 3)  # 繪製圓心
    else:
        print("No circles detected.")  # 若沒有檢測到圓形則輸出提示訊息
    cv2.imshow("Original Image", img1)  # 原圖
    cv2.imshow("Circle Detection", img2)  # Circle後
    cv2.waitKey(0)
