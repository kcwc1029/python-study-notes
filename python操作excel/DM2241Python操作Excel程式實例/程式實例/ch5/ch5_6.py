# ch5_6.py
import openpyxl

fn = "data5_1.xlsx"
wb = openpyxl.load_workbook(fn,data_only=True)
ws = wb.active
length = ws.max_row + 1
for i in range(3,length):
    ws.delete_rows(3)
wb.save("out5_6.xlsx")




