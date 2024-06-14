# ch5_3.py
import openpyxl

fn = "data5_1.xlsx"
wb = openpyxl.load_workbook(fn,data_only=True)
ws = wb.active
row = 0;
for i in range(4,8):
    ws.insert_rows(i+row,1)
    row = row + 1
wb.save("out5_3.xlsx")




