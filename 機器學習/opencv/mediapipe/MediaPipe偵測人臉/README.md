# 使用 MediaPipe 進行人臉偵測

MediaPipe 人臉檢測器任務可讓您檢測圖像或視頻中的人臉。您可以使用該任務來定位幀內的人臉和面部特征。該任務使用機器學習 (ML) 模型，可處理單張圖像或連續圖像流。該任務可輸出人臉位置以及以下面部關鍵點：左眼、右眼、鼻尖、嘴巴、左眼尾跡和右眼尾跡。

![upgit_20240503_1714714232.png](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2024/05/upgit_20240503_1714714232.png)

## 使用工具

-   Python
-   OpenCV (cv2)
-   NumPy
-   MediaPipe

## 使用方法

1. 確保已安裝所需的 Python 套件 (OpenCV、NumPy、MediaPipe)。
2. 將提供的 `blaze_face_short_range.tflite` 模型檔案放置在正確的路徑。
3. 執行程式碼。
4. 按下 `q` 鍵結束程式。

## 參數設定

該程式碼中有幾個可調整的參數:

### FaceDetectorOptions

```python
options = FaceDetectorOptions(
    base_options=BaseOptions(model_asset_path='./blaze_face_short_range.tflite'),
    running_mode=VisionRunningMode.IMAGE)
```

-   `model_asset_path`: 指定 TensorFlow Lite 模型檔案路徑。
-   `running_mode`: 可選擇 `IMAGE`、`VIDEO` 或 `LIVE_STREAM`，但因為會影響到其他呼叫，就不要動了。
