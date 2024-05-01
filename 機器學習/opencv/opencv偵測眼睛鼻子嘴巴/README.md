![upgit_20240501_1714549575.png](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2024/05/upgit_20240501_1714549575.png)

# 人臉特徵偵測

這個 Python 程式可以偵測影像或視訊中人臉的眼睛、嘴巴和鼻子,並將它們用不同顏色的方框標記出來。程式使用了 OpenCV 函式庫進行影像處理和特徵偵測。

## 使用工具

-   Python
-   OpenCV (cv2)

## 使用方法

### 偵測影像

1. 將需要偵測的影像檔案放置在與程式碼相同的目錄下。
2. 在程式碼中指定影像檔案名稱:

```python
img = cv2.imread('影像檔案名稱.jpg')
```

3. 執行程式碼。
4. 程式會在影像上標記出偵測到的眼睛(綠色方框)、嘴巴(紅色方框)和鼻子(藍色方框)。
5. 按下任意鍵即可關閉顯示的視窗。

### 偵測視訊

1. 確保已連接攝影機或視訊來源。
2. 執行程式碼。
3. 程式會開啟攝影機視訊,並在視訊影像上標記出偵測到的眼睛(綠色方框)、嘴巴(紅色方框)和鼻子(藍色方框)。
4. 按下 `q` 鍵即可退出程式。

## 可調整的參數

### 縮放因子 (`scaleFactor`)

```python
eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
```

縮放因子控制了在不同影像尺度下進行偵測的程度。較大的縮放因子會加快偵測速度,但可能會降低偵測精度。通常,設置在 1.1 到 1.4 之間是一個不錯的選擇。

### 最小鄰居數 (`minNeighbors`)

```python
eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
```

最小鄰居數用於控制偵測物件的質量。它指定了一個矩形必須被多少個鄰近矩形支持才能被確認為物件。較高的值可以提高偵測精度,但可能會導致一些物件被忽略。

### 最小和最大物件尺寸 (`minSize` 和 `maxSize`)

```python
eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), maxSize=(200, 200))
```

這些參數可以用來限制要偵測的物件尺寸範圍,從而排除一些不相關的偵測結果。例如,如果您知道要偵測的眼睛大小範圍在 30x30 到 200x200 像素之間,可以設置這些參數來提高精度。

### 使用不同的偵測模型

除了內建的模型外,您也可以使用自己訓練的模型進行偵測。只需將模型 XML 文件路徑傳遞給 `CascadeClassifier` 即可。

```python
custom_model = cv2.CascadeClassifier("path/to/custom_model.xml")
detections = custom_model.detectMultiScale(gray, ...)
```
