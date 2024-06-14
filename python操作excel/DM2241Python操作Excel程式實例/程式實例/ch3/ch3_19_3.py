# ch3_19_3.py
import openpyxl

fn = 'data3_19_1.xlsx'
wb = openpyxl.load_workbook(fn)
ws = wb.active
for col in ws.iter_cols(min_row=2,max_row=3,min_col=2,max_col=3):
    for cell in col:
        print(cell.value, end=' ')
    print()



