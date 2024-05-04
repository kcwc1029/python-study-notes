# 手掌偵測與視覺化

這個程式使用 OpenCV、NumPy 和 MediaPipe 庫來進行手掌偵測和視覺化。它能夠在攝影機影像或影片中偵測手掌,並繪製手掌骨架和檢測手勢。
![upgit_20240504_1714810883.png](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2024/05/upgit_20240504_1714810883.png)

## 使用工具

-   OpenCV: 用於影像處理和視覺化。
-   NumPy: 用於數值運算和影像處理。
-   MediaPipe: Google 開發的機器學習解決方案,用於手掌偵測和地標檢測。

## 使用方法

-   確保已安裝所需的 Python 庫 (OpenCV、NumPy 和 MediaPipe)。
-   將手掌偵測模型 `hand_landmarker.task` 放置在程式所在的目錄中。
-   執行程式`main_odd_version.py`(目前是覺得舊版比新版好用拉....)

## 手掌辨識標籤

![upgit_20240504_1714806374.png](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2024/05/upgit_20240504_1714806374.png)

## 參數說明

-   `num_hands`: 最多偵測的手掌數量,預設為 2。
-   `model_asset_path`: 手掌偵測模型路徑,預設為 `'./hand_landmarker.task'`。
-   `running_mode`: 運行模式,可選擇 `IMAGE` (影像模式) 或 `VIDEO` (影片模式)。(維持 IMAGE 即可)
-   `MARGIN`: 文字邊距 (像素),預設為 10。
-   `FONT_SIZE`: 文字大小,預設為 1。
-   `FONT_THICKNESS`: 文字粗細,預設為 1。
-   `HANDEDNESS_TEXT_COLOR`: 手勢文字顏色,預設為 `(88, 205, 54)`。

程式會自動開啟攝影機 (或指定的影片檔案),並在視窗中顯示偵測到的手掌骨架和手勢文字。按下 `q` 鍵可以退出程式。
