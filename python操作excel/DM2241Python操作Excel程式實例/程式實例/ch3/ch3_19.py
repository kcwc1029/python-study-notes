# ch3_19.py
import openpyxl

fn = 'data3_16.xlsx'
wb = openpyxl.load_workbook(fn)
ws = wb.active
for col in ws.columns:
    for cell in col:
        print(cell.value, end=' ')
    print()



