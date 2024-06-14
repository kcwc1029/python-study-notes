# ch10_6.py
import openpyxl
from openpyxl.formatting.rule import IconSet, FormatObject
from openpyxl.formatting.rule import Rule

fn = "data10_3.xlsx"
wb = openpyxl.load_workbook(fn)
ws = wb.active

# 建立 FormatObject 串列
start = FormatObject(type='percent',val=0)
second = FormatObject(type='percent',val=25)
third = FormatObject(type='percent',val=50)
end = FormatObject(type='percent',val=75)
cfvos = [start,second,third,end]
# 建立 IconSet 物件, 建立 Rule1 物件和執行設定 1
iconset = IconSet(iconSet='4Arrows', cfvo=cfvos,
                  showValue=None, reverse=None)
rule = Rule(type='iconSet', iconSet=iconset)
ws.conditional_formatting.add("A1:A10", rule)

# 建立 IconSet 物件, 建立 Rule2 物件和執行設定 2
iconset_obj = IconSet(iconSet='4Rating',cfvo=cfvos,
                      showValue=None,reverse=None)
rule2 = Rule(type='iconSet',iconSet=iconset_obj)                             
ws.conditional_formatting.add('B1:B10',rule2)

# 建立 IconSet 物件, 建立 Rule3 物件和執行設定 3
iconset_obj = IconSet(iconSet='4TrafficLights',cfvo=cfvos,
                      showValue=None,reverse=None)
rule3 = Rule(type='iconSet',iconSet=iconset_obj)                             
ws.conditional_formatting.add('C1:C10',rule3)

# 建立 IconSet 物件, 建立 Rule4 物件和執行設定 4
iconset_obj = IconSet(iconSet='4ArrowsGray',cfvo=cfvos,
                      showValue=None,reverse=None)
rule4 = Rule(type='iconSet',iconSet=iconset_obj)                             
ws.conditional_formatting.add('E1:E10',rule4)
# 儲存結果
wb.save('out10_6.xlsx')


