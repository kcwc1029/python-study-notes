# ch15_1.py
import openpyxl
from openpyxl.chart import BarChart, Reference

wb = openpyxl.Workbook()
ws = wb.active
for i in range(1,9):
    ws.append([i])
# 建立資料來源
data = Reference(ws,min_col=1,min_row=1,max_col=1,max_row=8)
chart = BarChart()          # 建立直條圖表物件
chart.add_data(data)        # 將資料加入圖表
ws.add_chart(chart,"C2")    # 將直條圖表加入工作表
# 儲存結果
wb.save('out15_1.xlsx')


