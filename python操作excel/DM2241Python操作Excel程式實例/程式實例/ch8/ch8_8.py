# ch8_8.py
import openpyxl

fn = "out8_6.xlsx"
wb = openpyxl.load_workbook(fn)
ws = wb.active
for i in range(2,9):
    index = 'B' + str(i)
    print(f"{index} : {ws[index].number_format}")






