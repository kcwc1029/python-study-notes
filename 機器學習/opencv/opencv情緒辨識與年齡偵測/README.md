# 人臉檢測與標注

此程序使用 OpenCV 從視頻流中讀取影像,並利用 DeepFace 庫對人臉進行情緒、年齡、種族和性別的檢測。檢測結果會使用 OpenCV 和 PIL 庫在影像上繪製和標注。

## 使用的工具

-   OpenCV: 用於讀取視頻流和顯示影像。
-   DeepFace: 基於深度學習的人臉分析工具,用於檢測人臉情緒、年齡、種族和性別。
-   PIL (Python Imaging Library): 用於在影像上繪製中文文字。

## 使用 Deepface 函式庫

如果是第一次使用 Deepface 函式庫，可先執行下方的程式碼 ( 圖片請搜尋一張人臉的圖片 )，執行後會額外下載一些人臉訓練的模型 ( 檔案大小總共可能快 2G )，下載後應該就能看到出現分析的參數，Deepface 分析的參數包含了情緒 ( emotion )、年齡 ( age )、性別 ( gender ) 和人種 ( race )。

安裝`pip install tf-keras`

```python
import cv2
from deepface import DeepFace
import numpy as np

img = cv2.imread('./lady.jpg')     # 讀取圖片
try:
    analyze = DeepFace.analyze(img)  # 辨識圖片人臉資訊
    print(analyze)
except:
    pass

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

1. 準備一個視頻文件(如`臉部偵測.mp4`)並將其放置在與程序相同的目錄下。
2. 如果需要在影像上顯示中文字,請準備一個中文字體文件(如`NotoSerifTC-Regular.otf`)並將其放置在與程序相同的目錄下。
3. 執行程序,它會從視頻流中讀取每一幀影像,對影像中的人臉進行檢測和分析。
4. 程序會在影像上繪製檢測結果,包括情緒(emotion)、年齡(age)、種族(race)和性別(gender)。
5. 按下`q`鍵可以退出程序。
