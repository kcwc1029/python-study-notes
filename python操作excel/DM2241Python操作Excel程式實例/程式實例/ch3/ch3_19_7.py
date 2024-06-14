# ch3_19_7.py
import openpyxl

fn = 'data3_19_1.xlsx'
wb = openpyxl.load_workbook(fn)
ws = wb.active
for col in ws.iter_cols(values_only=True):
    print(type(col))
    print(col)
   



