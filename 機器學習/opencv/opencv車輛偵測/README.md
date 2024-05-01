# 車輛偵測

這個 Python 程式可以從視訊中偵測出車輛,並將它們用綠色方框標記出來。程式使用了 OpenCV 函式庫進行影像處理和車輛偵測。

## DEMO

![upgit_20240501_1714552913.png](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2024/05/upgit_20240501_1714552913.png)

https://imgur.com/odFNEBb

## 使用工具

-   Python
-   OpenCV (cv2)

## 使用方法

1. 將需要偵測的視訊檔案 (例如 `car.mp4`) 放置在與程式碼相同的目錄下。
2. 在程式碼中指定視訊檔案名稱:

```python
cap = cv2.VideoCapture("視訊檔案名稱.mp4")
```

3. 執行程式碼。
4. 程式會開啟視訊,並在影像上標記出偵測到的車輛(綠色方框)。
5. 按下 `q` 鍵即可退出程式。

## 可調整的參數

### 縮放因子 (`scaleFactor`)

```python
cars = car.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
```

縮放因子控制了在不同影像尺度下進行偵測的程度。較大的縮放因子會加快偵測速度,但可能會降低偵測精度。通常,設置在 1.1 到 1.4 之間是一個不錯的選擇。

### 最小鄰居數 (`minNeighbors`)

```python
cars = car.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
```

最小鄰居數用於控制偵測物件的質量。它指定了一個矩形必須被多少個鄰近矩形支持才能被確認為物件。較高的值可以提高偵測精度,但可能會導致一些物件被忽略。

### 最小和最大物件尺寸 (`minSize` 和 `maxSize`)

```python
cars = car.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), maxSize=(200, 200))
```

這些參數可以用來限制要偵測的物件尺寸範圍,從而排除一些不相關的偵測結果。例如,如果您知道要偵測的車輛大小範圍在 30x30 到 200x200 像素之間,可以設置這些參數來提高精度。

### 使用不同的偵測模型

除了內建的模型外,您也可以使用自己訓練的模型進行偵測。只需將模型 XML 文件路徑傳遞給 `CascadeClassifier` 即可。

```python
custom_model = cv2.CascadeClassifier("path/to/custom_model.xml")
detections = custom_model.detectMultiScale(gray, ...)
```
