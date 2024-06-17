# ch1_3.py
import openpyxl

fn = 'sales.xlsx'
wb = openpyxl.load_workbook(fn)
print("預設的工作表名稱 = ", wb.active.title)
ws = wb['2025Q3']     # 設定特定工作表的名稱
print("特定工作表的名稱 = ", ws.title)






