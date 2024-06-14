# ch17_6.py
import openpyxl
from openpyxl.chart import BubbleChart, Series
from openpyxl.chart import Reference
from openpyxl.drawing.fill import GradientStop
from openpyxl.drawing.fill import GradientFillProperties
from openpyxl.drawing.fill import LinearShadeProperties

fn = "data17_6.xlsx"
wb = openpyxl.load_workbook(fn)
ws = wb.active

chart = BubbleChart()
chart.style = 40
chart.title = "2025年和2026年冰品銷售與獲利調查表"

# 建立系列物件 s
# 建立 x 軸資料 xvalues
xvalues = Reference(ws,min_col=3,max_col=8,min_row=3)
# 建立 y 軸資料 yvalues
yvalues = Reference(ws,min_col=3,max_col=8,min_row=4)
# 建立 z 軸資料 size, 這是氣泡的大小
size = Reference(ws,min_col=3,max_col=8,min_row=5)
s = Series(values=yvalues,xvalues=xvalues,zvalues=size,
           title="2025年")
# 將系列物件 s 加入氣泡圖物件
chart.series.append(s)
# 建立漸層色彩的 3D 氣泡圖
s.bubble3D = True
# 定義 3D 色彩漸變的位置和色彩
gs1 = GradientStop(pos=10000, prstClr="red")
gs2 = GradientStop(pos=50000, prstClr="yellow")
gs3 = GradientStop(pos=90000, prstClr="green")
# 定義漸變色彩物件和色彩方法
gprop = GradientFillProperties()           # 定義漸變色彩物件
gprop.stop_list = [gs1, gs2, gs3]          # 見變色位置和色彩定義
gprop.linear = LinearShadeProperties(90)   # 使用線性漸變色彩方法
# 將設定完成的漸變色彩應用到氣泡物
s.graphicalProperties.gradFill = gprop

# 建立系列物件 s1
# 建立 x 軸資料 xvalues
xvalues = Reference(ws,min_col=3,max_col=8,min_row=8)
# 建立 y 軸資料 yvalues
yvalues = Reference(ws,min_col=3,max_col=8,min_row=9)
# 建立 z 軸資料 size, 這是氣泡的大小
size = Reference(ws,min_col=3,max_col=8,min_row=10)
s1 = Series(values=yvalues,xvalues=xvalues,zvalues=size,
            title="2026年")
# 將系列物件 s 加入氣泡圖物件
chart.series.append(s1)
# 建立 3D 氣泡圖
s1.bubble3D = True

# 將氣泡圖物件加入工作表, 放在 B7
ws.add_chart(chart,"J2")
wb.save("out17_6.xlsx")


