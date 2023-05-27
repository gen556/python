import cv2
import numpy as np

# 載入圖像
img = cv2.imread('osaka.jpg')

# 創建一個空的掩膜
mask = np.zeros(img.shape[:2], np.uint8)

# 創建一個矩形選擇器
rect = cv2.selectROI(img)

# 創建兩個類別的直方圖
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)

# 執行GrabCut分割
cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

# 創建一個掩膜，將分割結果中被標記為前景或可能前景的像素設置為1
mask2 = np.where((mask == cv2.GC_FGD) | (
    mask == cv2.GC_PR_FGD), 1, 0).astype('uint8')

# 將原圖像與掩膜相乘，得到分割結果
result = img * mask2[:, :, np.newaxis]

# 顯示結果
cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
