# ch3_19_2.py
import openpyxl

fn = 'data3_19_1.xlsx'
wb = openpyxl.load_workbook(fn)
ws = wb.active
for row in ws.iter_rows(min_row=2,max_row=3,min_col=2,max_col=3):
    for cell in row:
        print(cell.value, end=' ')
    print()



