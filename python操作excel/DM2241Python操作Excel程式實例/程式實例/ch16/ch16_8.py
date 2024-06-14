# ch16_8.py
import openpyxl
from openpyxl.chart import LineChart, Reference
from openpyxl.utils.units import pixels_to_EMU

wb = openpyxl.Workbook()                # 開啟活頁簿
ws = wb.active                          # 獲得目前工作表
rows = [
    ['', 'Benz', 'BMW', 'Audi'],
    ['2025年', 400, 300, 250],
    ['2026年', 350, 250, 300],
    ['2027年', 500, 300, 450],
    ['2028年', 300, 250, 420],
    ['2029年', 200, 350, 270]]
for row in rows:
    ws.append(row)
    
# 建立資料來源
data = Reference(ws,min_col=2,max_col=4,min_row=1,max_row=6)    
# 建立折線圖物件
chart = LineChart()                      # 折線圖
# 將資料加入圖表
chart.add_data(data, titles_from_data=True) # 建立圖表
# 建立圖表和座標軸標題
chart.title = '汽車銷售表'                # 圖表標題
chart.x_axis.title = '年度'               # x軸標題
chart.y_axis.title = '銷售數'             # y軸標題
# x軸資料標籤 (年度)
xtitle = Reference(ws,min_col=1,min_row=2,max_row=6)         
chart.set_categories(xtitle)
# 建立線條資料點標記和樣式
# 線條編號 0 標記
s0 = chart.series[0]                      # 線條編號 0 - Benz
s0.marker.symbol = "diamond"
s0.marker.size = 8
s0.marker.graphicalProperties.solidFill = 'FF0000'       # 標記內部
s0.marker.graphicalProperties.line.solidFill = 'FF0000'  # 標記輪廓
# 線條編號 0 樣式
s0.graphicalProperties.line.solidFill = '00AAAA'         
s0.graphicalProperties.line.dashStyle = "dashDot"
s0.graphicalProperties.line.width = pixels_to_EMU(3)
# 線條編號 1 標記
s1 = chart.series[1]                      # 線條編號 1 - BMW
s1.marker.symbol = "circle"
s1.marker.size = 5
s1.marker.graphicalProperties.solidFill = '00FF00'       # 標記內部
s1.marker.graphicalProperties.line.solidFill = '00FF00'  # 標記輪廓
# 線條編號 1 樣式
s1.graphicalProperties.line.noFill = True         


# 線條編號 2 標記
s2 = chart.series[2]                      # 線條編號 2 - Audi
s2.marker.symbol = "star"
s2.marker.size = 10
s2.marker.graphicalProperties.solidFill = '0000FF'       # 標記內部
s2.marker.graphicalProperties.line.solidFill = '0000FF'  # 標記輪廓
# 線條編號 2 樣式
s2.graphicalProperties.line.solidFill = 'FFA500'       
s2.graphicalProperties.line.dashStyle = "dash"         
s2.graphicalProperties.line.width = pixels_to_EMU(3) 
# 將圖表放在工作表 E1
ws.add_chart(chart, 'E1')      
wb.save('out16_8.xlsx')







