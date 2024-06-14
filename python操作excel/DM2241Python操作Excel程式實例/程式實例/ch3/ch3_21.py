# ch3_21.py
import openpyxl

fn = 'data3_16.xlsx'
wb = openpyxl.load_workbook(fn)
ws = wb.active
for row in ws['A1':'E9']:
    for cell in row:
        print(cell.value, end=' ')
    print()




