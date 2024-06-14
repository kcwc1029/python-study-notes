# ch15_6.py
import openpyxl
from openpyxl.chart import BarChart, Reference

wb = openpyxl.Workbook()                # 開啟活頁簿
ws = wb.active                          # 獲得目前工作表
rows = [
    ['', '2025年', '2026年'],
    ['亞洲', 100, 300],
    ['歐洲', 400, 600],
    ['美洲', 500, 700],
    ['非洲', 200, 100]]
for row in rows:
    ws.append(row)
    
# 建立資料來源
data = Reference(ws,min_col=2,max_col=3,min_row=1,max_row=5)    
# 建立直條圖物件
chart = BarChart()                      # 直條圖
# 將資料加入圖表
chart.add_data(data, titles_from_data=True) # 建立圖表
# 建立圖表和座標軸標題
chart.title = '深智軟體銷售表'          # 圖表標題
chart.x_axis.title = '地區'             # x軸標題
chart.y_axis.title = '業績金額'         # y軸標題
# x軸資料標籤 (亞洲歐洲美洲非洲)
xtitle = Reference(ws,min_col=1,min_row=2,max_row=5)         
chart.set_categories(xtitle)
# 設定長條圖表色彩樣式
chart.style = 48
# 將圖表放在工作表 E1
ws.add_chart(chart, 'E1')      
wb.save('out15_6.xlsx')







