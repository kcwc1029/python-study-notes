# ch10_5.py
import openpyxl
from openpyxl.formatting.rule import IconSetRule

fn = "data10_3.xlsx"
wb = openpyxl.load_workbook(fn)
ws = wb.active
# 建立 A1:A10 資料橫條
rule1 = IconSetRule(icon_style='3Flags',
                    type='percent',
                    values=[0,33,67],reverse=None)
ws.conditional_formatting.add("A1:A10",rule1)

# 建立 B1:B10 資料橫條
rule2 = IconSetRule(icon_style='3TrafficLights1',
                    type='percent',
                    values=[0,33,67],reverse=None)
ws.conditional_formatting.add("B1:B10",rule2)

# 建立 B1:B10 資料橫條
rule3 = IconSetRule(icon_style='4Arrows',
                    type='percent',
                    values=[0,25,50,75],reverse=None)
ws.conditional_formatting.add("C1:C10",rule3)

# 建立 E1:E10 資料橫條
rule4 = IconSetRule(icon_style='5Rating',
                    type='percent',
                    values=[0,20,40,60,80],reverse=None)
ws.conditional_formatting.add("E1:E10", rule4)

wb.save('out10_5.xlsx')            # 將活頁簿儲存





