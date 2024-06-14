# ch5_10.py
import openpyxl

fn = "data5_10.xlsx"
wb = openpyxl.load_workbook(fn)
ws = wb.active
ws.delete_cols(3)
wb.save("out5_10.xlsx")




