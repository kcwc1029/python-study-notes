# 人臉特征繪制工具

這個工具使用了 MediaPipe 庫來檢測圖像或視頻中的人臉，並在檢測到的人臉上繪制特征點和輪廓。

![upgit_20240503_1714721530.png](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2024/05/upgit_20240503_1714721530.png)

## 工具

-   OpenCV：用於圖像處理和顯示。
-   NumPy：用於數值計算和數組操作。
-   MediaPipe：用於人臉檢測和特征繪制。

## 使用方法

1. 安裝依賴庫：

```
pip install opencv-python mediapipe
```

2. 下載 MediaPipe 的模型文件，可以從 [MediaPipe GitHub](https://github.com/google/mediapipe) 上找到。
3. 將模型文件保存到項目目錄，並修改代碼中的 `model_asset_path` 為模型文件的路徑。
4. 運行代碼，傳入視頻文件路徑或攝像頭索引來進行人臉特征繪制。

## 可調參數

-   `FACEMESH_TESSELATION`：繪制人臉網格。
-   `FACEMESH_CONTOURS`：繪制人臉輪廓。
-   `FACEMESH_IRISES`：繪制眼睛虹膜。
-   `FACEMESH_LEFT_EYE`：繪制左眼。
-   `FACEMESH_RIGHT_EYE`：繪制右眼。
-   `FACEMESH_LEFT_EYEBROW`：繪制左眉。
-   `FACEMESH_RIGHT_EYEBROW`：繪制右眉。
-   `FACEMESH_LIPS`：繪制嘴唇。

## 完整臉部辨識標籤：

https://github.com/google/mediapipe/blob/master/mediapipe/modules/face_geometry/data/canonical_face_model_uv_visualization.png
