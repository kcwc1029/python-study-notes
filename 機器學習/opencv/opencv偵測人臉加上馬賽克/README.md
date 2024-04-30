這個 Python 程式可以偵測影像中的人臉,並將人臉區域模糊化(馬賽克效果)。程式使用 OpenCV 函式庫進行影像處理和人臉偵測。

## DEMO

![upgit_20240501_1714499729.png](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2024/05/upgit_20240501_1714499729.png)

## usage

可調整的參數：

-   使用不同的人臉偵測模型：'face_cascade = cv2.CascadeClassifier("模型檔案路徑")'
-   馬賽克程度 (level)，level 越小,馬賽克效果越明顯;level 越大,馬賽克效果越微弱。您可以根據需求調整這個參數。
    'level = 15 # 馬賽克程度'
-   人臉偵測參數：detectMultiScale 函數的第二個和第三個參數分別控制了圖像遮罩的放大倍數和偵測物件的最小相鄰矩形個數。您可以調整這些參數來優化人臉偵測效果。
    'faces = face_cascade.detectMultiScale(gray, 1.2, 3)'
