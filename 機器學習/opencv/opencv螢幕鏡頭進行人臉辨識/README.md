![upgit_20240427_1714151521.png](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2024/04/upgit_20240427_1714151521.png)

這個 Python 程式碼使用 OpenCV 函式庫來進行人臉偵測。它可以從視訊串流或視訊檔案中偵測人臉並在每個偵測到的人臉周圍繪製一個綠色方框。

## 使用方式

1. 確保您已經安裝了 OpenCV 函式庫。
2. 將 face_detact.xml 檔案放置在與程式碼相同的目錄中。這是 OpenCV 預先訓練的人臉偵測分類器。
3. 如果要使用網路攝影機進行人臉偵測,請取消註釋 `cap = cv.VideoCapture(0)` 這行。
4. 如果要使用視訊檔案進行人臉偵測,請取消註釋 `cap = cv.VideoCapture("./people.mp4")` 這行,並將 `"./people.mp4"` 改為您要使用的視訊檔案路徑。

## demo 

https://imgur.com/gallery/HJOfRyf
