import numpy as np
import cv2
import math

img1 = cv2.imread("osaka.jpg", -1)  # 讀取
if img1 is None:  # 檢查讀取
    print("Error: Failed to read image file")
else:
    img2 = img1.copy()  # 複製圖1
    gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)  # 灰階化
    edges = cv2.Canny(gray, 200, 500)  # 用Canny偵測邊緣點
    line = cv2.HoughLines(edges, 1, math.pi/180.0, 120)  # 至少120像素點
    if line is not None:  # 有線的話
        a, b, c = line.shape
        for i in range(a):
            rho = line[i][0][0]  # 設置點rho
            theta = line[i][0][1]  # 設置弧度theta
            a = math.cos(theta)  # cosΘ
            b = math.sin(theta)  # sinΘ
            x0, y0 = a*rho, b*rho  # 決定點
            pt1 = (int(x0+1000*(-b)), (int(y0+1000*(a))))  # 設定點一
            pt2 = (int(x0-1000*(-b)), (int(y0-1000*(a))))  # 設定點二
            cv2.line(img2, pt1, pt2, (255, 0, 0), 1, cv2.LINE_AA)  # 在img2上畫線
    cv2.imshow("Original Image", img1)  # 原圖
    cv2.imshow("canny Image", edges)  # canny
    cv2.imshow("Hough Line", img2)
    cv2.waitKey(0)
