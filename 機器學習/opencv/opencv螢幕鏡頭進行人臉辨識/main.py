# NOTE: 無法在colab上面運作，要額外拉anaconda的核心來做
import cv2 as cv
import numpy as np


# cap = cv.VideoCapture(0)  # 從網路攝影機讀取視訊串流
cap = cv.VideoCapture("./people.mp4")  # 從視訊檔案讀取

while True:
    ret, frame = cap.read() # 布林值 圖像偵
    if ret:
        frame = cv.resize(frame, (600, 600))  # 調整影像大小
        # 將影像轉換為灰階
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # 載入預先訓練的人臉偵測分類器
        facecascade = cv.CascadeClassifier("./face_detact.xml")
        # 偵測灰階影像中的人臉
        faceRect = facecascade.detectMultiScale(gray, 1.1, 3)
        print(len(faceRect)) # 印出偵測到的人臉數量

        # 在每個偵測到的人臉周圍繪製綠色方框
        for (x, y, w, h) in faceRect:
            cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv.imshow("frame", frame) # 顯示圖像
    if cv.waitKey(1) != -1: # 按q退出
        break

cap.release() # 釋放攝像頭資源，即關閉攝像頭設備
cv.destroyAllWindows() # 關閉所有 OpenCV 窗口
