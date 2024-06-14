# ch18_7.py
import openpyxl
from openpyxl.chart import PieChart3D, Reference
from openpyxl.chart.series import DataLabelList
from openpyxl.chart.series import DataPoint

wb = openpyxl.Workbook()            
ws = wb.active                      # 目前工作表
rows = [
    ['地區', '人次'],
    ['上海', 300],
    ['東京', 600],
    ['香港', 700],
    ['新加坡', 400]]
for row in rows:
    ws.append(row)

chart = PieChart3D()                # 3D圓餅圖
chart.title = '深智員工旅遊意向調查表'
chart.style = 26
# 設定資料來源
data = Reference(ws,min_col=2,min_row=1,max_row=5)
# 將資料加入圓餅圖物件
chart.add_data(data,titles_from_data=True)
# 設定標籤資料
labels = Reference(ws,min_col=1,min_row=2,max_row=5)   
chart.set_categories(labels)        # 設定標籤名稱
# 顯示切片百分比
chart.dataLabels = DataLabelList()
chart.dataLabels.showPercent = True
# 圓餅切片色彩串列
colors = ['00FFFF','FF0000','00FF00','FFFF00']
# 取得切片元素, 所有元素
slices = [DataPoint(idx=i) for i in range(4)]
# 因為只有一組資料, 所以是第0系列, 所有原素
chart.series[0].data_points = slices    
# 設定所有切片的顏色
for i in range(4):
    slices[i].graphicalProperties.solidFill = colors[i]
ws.add_chart(chart,'D1')            # 將圖表加入工作表
wb.save('out18_7.xlsx')





