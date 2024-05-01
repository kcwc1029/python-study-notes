# 行人偵測

這個 Python 程式可以從視訊中偵測出行人,並將他們用綠色方框標記出來。程式使用了 OpenCV 函式庫進行影像處理和行人偵測。

## 使用工具

-   Python
-   OpenCV (cv2)

## DEMO

![upgit_20240501_1714554235.png](https://raw.githubusercontent.com/kcwc1029/obsidian-upgit-image/main/2024/05/upgit_20240501_1714554235.png)

## 使用方法

1. 將需要偵測的視訊檔案 (例如 `行人1.mp4`) 放置在與程式碼相同的目錄下。
2. 在程式碼中指定視訊檔案名稱:

```python
cap = cv2.VideoCapture("視訊檔案名稱.mp4")
```

3. 執行程式碼。
4. 程式會開啟視訊,並在影像上標記出偵測到的行人(綠色方框)。
5. 按下 `q` 鍵即可退出程式。

## 可調整的參數

### 縮放因子 (`scaleFactor`)

```python
cars = car.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=2)
```

縮放因子控制了在不同影像尺度下進行偵測的程度。較大的縮放因子會加快偵測速度,但可能會降低偵測精度。通常,設置在 1.1 到 1.4 之間是一個不錯的選擇。

### 最小鄰居數 (`minNeighbors`)

```python
cars = car.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=2)
```

最小鄰居數用於控制偵測物件的質量。它指定了一個矩形必須被多少個鄰近矩形支持才能被確認為物件。較高的值可以提高偵測精度,但可能會導致一些物件被忽略。

### 最小和最大物件尺寸 (`minSize` 和 `maxSize`)

```python
cars = car.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=2, minSize=(30, 60), maxSize=(200, 400))
```
