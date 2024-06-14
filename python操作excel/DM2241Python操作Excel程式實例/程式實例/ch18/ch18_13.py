# ch18_13.py
import openpyxl
from openpyxl.chart import RadarChart, Reference

fn = "data18_13.xlsx"
wb = openpyxl.load_workbook(fn)            
ws = wb.active                      

chart = RadarChart()
chart.title = "飲料市調表"
chart.style = 26
# 設定資料來源
data = Reference(ws, min_col=2,max_col=4,min_row=1,max_row=6)
# 將資料加入雷達圖物件
chart.add_data(data,titles_from_data=True)
# 設定標籤資料
labels = Reference(ws, min_col=1,min_row=2,max_row=6)
chart.set_categories(labels)

ws.add_chart(chart, "E1")
wb.save('out18_13.xlsx')





