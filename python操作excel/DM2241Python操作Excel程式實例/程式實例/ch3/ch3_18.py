# ch3_18.py
import openpyxl

fn = 'data3_16.xlsx'
wb = openpyxl.load_workbook(fn)
ws = wb.active
for row in ws.rows:
    for cell in row:
        print(cell.value, end=' ')
    print()



