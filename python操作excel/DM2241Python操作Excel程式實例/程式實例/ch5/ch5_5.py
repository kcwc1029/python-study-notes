# ch5_5.py
import openpyxl

fn = "data5_1.xlsx"
wb = openpyxl.load_workbook(fn)
ws = wb.active

ws.delete_rows(4)
wb.save("out5_5.xlsx")




