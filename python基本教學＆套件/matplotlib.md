```python
引入
import matplotlib.pyplot as plt
```

## 散布圖 Scatter Chart

＄ pyplot.scatter() 參數說明

| 參數         | 說明                                                                                                                                                   |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| x          | 必填，第一組數據 ( x 軸 )。                                                                                                                                    |
| y          | 必填，第二組數據 ( y 軸 )。                                                                                                                                    |
| c          | 資料點的顏色，支援陣列資料 ( 除了十六進位色碼，也可填入顏色代碼，例如 r、g、b、m、c、y...等，參考：color 列表 )。[參考 color map](https://matplotlib.org/stable/users/explain/colors/colormaps.html) |
| s          | 資料點的尺寸，預設和資料同大小，支援陣列資料。                                                                                                                              |
| marker     | 資料點樣式，預設圓點 [參考 color market](https://matplotlib.org/stable/api/markers_api.html#module-matplotlib.markers)                                           |
| cmap       | 顏色地圖，如果 c 為數據資料，會根據 c 的數據對應指定顏色 ( 參考：colormaps )。                                                                                                    |
| vmin       | 對照顏色地圖的最小值。                                                                                                                                          |
| vmax       | 對照顏色地圖的最大值。                                                                                                                                          |
| alpha      | 資料點透明度，預設 1，範圍 0 ( 完全透明 ) ～ 1 ( 完全不透明 )。                                                                                                             |
| linewidths | 資料點外框粗細，預設無外框，支援陣列資料。                                                                                                                                |
| edgecolors | 資料點外框顏色，預設無外框，顏色設定等同 c。                                                                                                                              |

```python
import matplotlib.pyplot as plt

# 元素
x = [1,2,3,4,5,6,7,8,9,10]
y = [11,8,26,16,9,17,23,4,14,10]

plt.scatter(x,y)
plt.show()
```

```python
import matplotlib.pyplot as plt

# 元素
x = [1,2,3,4,5,6,7,8,9,10]
y = [11,8,26,16,9,17,23,4,14,10]

# 設定顏色 c, cmap
# 顏色地圖是紅橙黃綠藍，則 0～20 對應紅色，21～40 對應橙色，41～60 對應黃色，61～80 對應綠色，81～100 對應藍色。
color_map = 'Set1'
color_size = [i*100 for i in y]

# 設定marker尺寸
size = [i*100 for i in y]
plt.scatter(x,y,s=color_size,c=color_size,cmap=color_map)  # 使用 Set1 的 colormap
plt.show()
```

```python

```

```python

```

```python

```

```python

```
