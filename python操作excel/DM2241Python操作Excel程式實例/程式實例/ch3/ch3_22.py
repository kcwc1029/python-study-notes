# ch3_22.py
import openpyxl

fn = 'data3_16.xlsx'
wb = openpyxl.load_workbook(fn)
ws = wb.active
data_range = ws['B':'D']
for cols in data_range:
    for cell in cols:
        print(cell.value, end=' ')
    print()




