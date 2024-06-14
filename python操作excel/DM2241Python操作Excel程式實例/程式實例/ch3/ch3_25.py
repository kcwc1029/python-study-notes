# ch3_25.py
import openpyxl

fn = 'data3_25.xlsx'
wb = openpyxl.load_workbook(fn)
ws = wb.active
print(ws.dimensions)






