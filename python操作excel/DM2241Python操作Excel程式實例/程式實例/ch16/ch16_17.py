# ch16_17.py
import openpyxl
from openpyxl.chart import AreaChart3D, Reference

wb = openpyxl.Workbook()                # 開啟活頁簿
ws = wb.active                          # 獲得目前工作表
rows = [
    ['', 'BMW', 'Benz'],
    ['2025年', 100, 400],
    ['2026年', 150, 350],
    ['2027年', 130, 500],
    ['2028年', 200, 600],
    ['2029年', 220, 450]]
for row in rows:
    ws.append(row)
    
# 建立資料來源
data = Reference(ws,min_col=2,max_col=3,min_row=1,max_row=6)    
# 建立3D區域圖物件
chart = AreaChart3D()                      # 3D區域圖
# 將資料加入圖表
chart.add_data(data, titles_from_data=True) # 建立圖表
# 建立圖表和座標軸標題
chart.title = '汽車銷售表'                # 圖表標題
chart.x_axis.title = '年度'               # x軸標題
chart.y_axis.title = '銷售數'             # y軸標題
# x軸資料標籤 (年度)
xtitle = Reference(ws,min_col=1,min_row=2,max_row=6)         
chart.set_categories(xtitle)
# 更改3D區域圖樣式
chart.style = 48
# 將圖表放在工作表 E1
ws.add_chart(chart, 'E1')      
wb.save('out16_17.xlsx')







