# ch1_4.py
import openpyxl

fn = 'sales.xlsx'
wb = openpyxl.load_workbook(fn)
print("預設的工作表名稱 = ", wb.active.title)
ws0 = wb.worksheets[0]
ws1 = wb.worksheets[1]
ws2 = wb.worksheets[2]
print("特定工作表的名稱 = ", ws0.title)
print("特定工作表的名稱 = ", ws1.title)
print("特定工作表的名稱 = ", ws2.title)





