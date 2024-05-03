![upgit_20240427_1714167211.png](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2024/04/upgit_20240427_1714167211.png)

這個 Python 程式碼使用 OpenCV 和 Google 的 MediaPipe 進行手部關鍵點的偵測和追蹤。它會從攝影機讀取影像,應用 MediaPipe 手部檢測模型來偵測手部並顯示其關鍵點。同時也會在影像上繪製手部輪廓和關節連線。

## 使用方式

1. 確保已安裝 OpenCV 和 MediaPipe 相關套件
2. 執行腳本 python hand_tracking.py
3. 按下任意鍵可結束程式

## 安裝 mediapipe 遇到問題

### 發生問題

在 mac 上面使用 mediapipe，但在執行一直抱錯

```
/Users/usera/Documents/Development/Apps/prj/.venv/bin/python /Users/usera/Documents/Development/Apps/prj/main.py

2024-02-24 17:53:59.478 python[83108:17726527] WARNING: AVCaptureDeviceTypeExternal is deprecated for Continuity Cameras. Please use AVCaptureDeviceTypeContinuityCamera and add NSCameraUseContinuityCameraDeviceType to your Info.plist.
Traceback (most recent call last):
  File "/Users/usera/Documents/Development/Apps/prj/main.py", line 8, in <module>
    hands = mpHands.Hands()
            ^^^^^^^^^^^^^^^
  File "/Users/usera/Documents/Development/Apps/prj/.venv/lib/python3.11/site-packages/mediapipe/python/solutions/hands.py", line 114, in __init__
    super().__init__(
  File "/Users/usera/Documents/Development/Apps/prj/.venv/lib/python3.11/site-packages/mediapipe/python/solution_base.py", line 248, in __init__
    self._graph = calculator_graph.CalculatorGraph(
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
RuntimeError: ValidatedGraphConfig Initialization failed.
ImageToTensorCalculator: ; RET_CHECK failure (mediapipe/calculators/tensor/image_to_tensor_calculator.cc:144) ValidateOptionOutputDims(options) returned INTERNAL: ; ...

Process finished with exit code 1
```

### 參考連結

https://github.com/google/mediapipe/issues/5168

### 處理方式

在參考連結有說，安裝 0.10.9 就好。好像 0.10.11 跟 0.10.10 都會有問題。所要要安裝特定版本 0.10.9

### 處理指令

```
移除目前版本
pip uninstall mediapipe

安裝特定版本
pip install mediapipe==0.10.9
```
