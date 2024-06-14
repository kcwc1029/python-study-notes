# ch8_9.py
import openpyxl

fn = "out8_7.xlsx"
wb = openpyxl.load_workbook(fn)
ws = wb.active
for i in range(2,8):
    index = 'B' + str(i)
    print(f"{index} : {ws[index].number_format}")






