# NOTE: 額外拉一個py出來做
import cv2
import numpy as np

# 轉換為灰度圖像
def rgb_to_gray(rgb_image):
    # 獲取圖像尺寸
    height, width, channel = rgb_image.shape
    
    # 創建一個空白的灰度圖像
    gray_image = np.zeros((height, width), dtype=np.uint8)
    
    # 遍歷圖像的每個像素
    for y in range(height):
        for x in range(width):            
            r, g, b = rgb_image[y, x] # 獲取當前像素的 RGB 值
            gray_value = int(0.3 * r + 0.59 * g + 0.11 * b) # 根據公式計算灰度值
            gray_image[y, x] = gray_value # 將灰度值設置到灰度圖像中

    return gray_image

# 讀取彩色圖像
color_image = cv2.imread("./TW.jpg")

if color_image is None:
    print("錯誤: 無法讀取圖像。")
else:
    gray_image = rgb_to_gray(color_image)
    
    # 顯示灰度圖像
    cv2.imshow("灰度圖像", gray_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()