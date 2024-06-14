# ch3_19_4.py
import openpyxl

fn = 'data3_19_1.xlsx'
wb = openpyxl.load_workbook(fn)
ws = wb.active
for row in ws.iter_rows():
    print(type(row))
    print(row)
   



