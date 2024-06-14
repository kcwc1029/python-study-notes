# ch18_1.py
import openpyxl
from openpyxl.chart import PieChart, Reference

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

chart = PieChart()                  # 圓餅圖
chart.title = '深智員工旅遊意向調查表'
# 設定資料來源
data = Reference(ws,min_col=2,min_row=1,max_row=5)
# 將資料加入圓餅圖物件
chart.add_data(data,titles_from_data=True)
# 設定標籤資料
labels = Reference(ws,min_col=1,min_row=2,max_row=5)   
chart.set_categories(labels)        # 設定標籤名稱
ws.add_chart(chart,'D1')            # 將圖表加入工作表
wb.save('out18_1.xlsx')





