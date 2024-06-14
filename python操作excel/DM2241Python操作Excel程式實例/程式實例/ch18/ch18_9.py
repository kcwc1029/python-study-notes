# ch18_9.py
import openpyxl
from openpyxl.chart import (
    DoughnutChart,
    Reference
)
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
chart.title = "2025年外銷統計表"
chart.style = 26                        # 類型 26
# 設定資料來源 --- 只用2025年資料
data = Reference(ws,min_col=2,min_row=1,max_row=5)
# 將資料加入環圈圖物件
labels = Reference(ws,min_col=1,min_row=2,max_row=5)
# 設定標籤資料
chart.add_data(data, titles_from_data=True)
chart.set_categories(labels)            # 設定標籤
ws.add_chart(chart, "E1")               # 將圖表加入工作表
wb.save("out18_9.xlsx")


