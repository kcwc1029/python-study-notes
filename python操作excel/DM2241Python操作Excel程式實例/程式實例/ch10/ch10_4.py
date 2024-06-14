# ch10_4.py
import openpyxl
from openpyxl.formatting.rule import DataBar, FormatObject
from openpyxl.formatting.rule import Rule

fn = "data10_3.xlsx"
wb = openpyxl.load_workbook(fn)
ws = wb.active

# 建立 FormatObject 串列
start = FormatObject(type='min')
end = FormatObject(type='max')
cfvos = [start, end]
# 建立 DataBar 物件, 建立 Rule1 物件和執行設定 1
databar_obj = DataBar(cfvo=cfvos,color='0000FF')
rule1 = Rule(type='dataBar',dataBar=databar_obj)                             
ws.conditional_formatting.add('A1:C10',rule1)

# 建立 DataBar 物件, 建立 Rule2 物件和執行設定 2
databar_obj = DataBar(cfvo=cfvos,color='00FF00')
rule2 = Rule(type='dataBar',dataBar=databar_obj)                             
ws.conditional_formatting.add('E1:E10',rule2)

# 儲存結果
wb.save('out10_4.xlsx')


