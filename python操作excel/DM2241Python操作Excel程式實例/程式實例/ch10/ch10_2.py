# ch10_2.py
import openpyxl
from openpyxl.styles import Color
from openpyxl.formatting.rule import ColorScale, FormatObject
from openpyxl.formatting.rule import Rule

fn = "data10_2.xlsx"
wb = openpyxl.load_workbook(fn)
ws = wb.active

# 建立FormatObject串列
start = FormatObject(type='min')
mid = FormatObject(type='num',val=6000)
end = FormatObject(type='max')
cfvos = [start, mid, end]
# 建立ColorObject串列
colors = [Color('FFFF00'),Color('F0F8FF'),Color('00FF00')]
# 建立ColorScale物件
colorscale_obj = ColorScale(cfvo=cfvos,color=colors)
# 建立Rule物件
rule = Rule(type='colorScale',colorScale=colorscale_obj)                             
# 執行設定
ws.conditional_formatting.add('C4:E10',rule)
# 儲存結果
wb.save('out10_2.xlsx')


