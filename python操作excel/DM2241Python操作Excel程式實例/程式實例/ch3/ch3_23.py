# ch3_23.py
import openpyxl

fn = 'data3_16.xlsx'
wb = openpyxl.load_workbook(fn)
ws = wb.active
data_range = ws[3:6]
for rows in data_range:
    for cell in rows:
        print(cell.value, end=' ')
    print()




