# ch3_19_5.py
import openpyxl

fn = 'data3_19_1.xlsx'
wb = openpyxl.load_workbook(fn)
ws = wb.active
for col in ws.iter_cols():
    print(type(col))
    print(col)
   



