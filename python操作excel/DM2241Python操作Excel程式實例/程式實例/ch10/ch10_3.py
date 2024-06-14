# ch10_3.py
import openpyxl
from openpyxl.formatting.rule import DataBarRule

fn = "data10_3.xlsx"
wb = openpyxl.load_workbook(fn)
ws = wb.active
# 建立 A1:C10 資料橫條
rule1 = DataBarRule(start_type='min',start_value=None,
                   end_type='max', end_value=None,
                   color="0000FF",
                   minLength=None, maxLength=None)
ws.conditional_formatting.add("A1:C10", rule1)

# 建立 E1:E10 資料橫條
rule2 = DataBarRule(start_type='min',start_value=None,
                   end_type='max', end_value=None,
                   color="00FF00",
                   minLength=None, maxLength=None)
ws.conditional_formatting.add("E1:E10", rule2)
wb.save('out10_3.xlsx')            # 將活頁簿儲存





