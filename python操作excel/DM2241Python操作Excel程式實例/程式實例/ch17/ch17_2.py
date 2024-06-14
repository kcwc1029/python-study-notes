# ch17_2.py
import openpyxl
from openpyxl.chart import ScatterChart, Series
from openpyxl.chart import Reference    

wb = openpyxl.Workbook()
ws = wb.active

rows = [
    ['溫度','台北','高雄'],
    [10, 80, 30],
    [15, 100, 50],
    [20, 150, 70],
    [25, 200, 120],
    [30, 320, 360],
    [35, 395, 550],
]
for row in rows:
    ws.append(row)
chart = ScatterChart()
chart.title = "台北與高雄冰品銷量統計表"
chart.style = 13
chart.x_axis.title = '溫度'
chart.y_axis.title = '冰品銷量'

# 建立系列的標記marker和顏色colors
marker = ['circle', 'diamond']
colors = ['FF0000', '0000FF']
# 建立 x 軸的參考資料
xvalues = Reference(ws,min_col=1,min_row=2,max_row=7)
# 分別處理每一個欄位的資料, 先台北, 然後高雄, ...
for i in range(2, 4):
    # 定義系列series的y軸參考資料
    values = Reference(ws,min_col=i,min_row=1,max_row=7)
    # 建立系列物件 s
    s = Series(values,xvalues,title_from_data=True)
    # 建立系列標記
    s.marker.symbol = marker[i-2]
    # 建立系列標記填充顏色
    s.marker.graphicalProperties.solidFill = colors[i-2]
    # 建立系列標記輪廓顏色
    s.marker.graphicalProperties.line.solidFill = colors[i-2]
    # 取消線條顯示
    s.graphicalProperties.line.noFill = True
    # 將系列物件 s 加入散點圖物件
    chart.series.append(s)
ws.add_chart(chart,"E1")
wb.save("out17_2.xlsx")


