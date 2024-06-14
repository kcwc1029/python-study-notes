# ch18_12.py
import openpyxl
from openpyxl.chart import (
    DoughnutChart,
    Reference,
    Series
)
from openpyxl.chart.series import DataPoint
from openpyxl.chart.series import DataLabelList
wb = openpyxl.Workbook()
ws = wb.active
data = [
    ['地區', '2025年', '2026年'],
    ['亞洲', 3500, 3800],
    ['歐洲', 1800, 2200],
    ['美洲', 2500, 3000],
    ['其他', 800, 1200],
]
for row in data:
    ws.append(row)

chart = DoughnutChart()                 # 環圈圖
chart.title = "2025年和2026年外銷統計表"
chart.style = 26                        # 類型 26
# 設定資料來源 --- 用2025和2026年資料
data = Reference(ws,min_col=2,max_col=3,min_row=1,max_row=5)
# 將資料加入環圈圖物件
labels = Reference(ws,min_col=1,min_row=2,max_row=5)
# 設定標籤資料
chart.add_data(data, titles_from_data=True)
chart.set_categories(labels)            # 設定標籤
# 顯示切片百分比
chart.dataLabels = DataLabelList()
chart.dataLabels.showPercent = True
# 圓餅切片色彩串列
colors = ['00FFFF','FF8A65','00FF00','FFFF00']
# 取得切片元素, 所有元素
slices = [DataPoint(idx=i) for i in range(4)]
# 有 2 組系列資料, 設定第 1 (從 0 起算)組所有原素
chart.series[1].data_points = slices    
# 設定所有切片的顏色
for i in range(4):
    slices[i].graphicalProperties.solidFill = colors[i]
    if i == 2:                          # 將索引 2 切片分離
        slices[i].explosion = 10
ws.add_chart(chart, "E1")               # 將圖表加入工作表
wb.save("out18_12.xlsx")


