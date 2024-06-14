# ch5_11.py
import openpyxl

fn = "data5_10.xlsx"
wb = openpyxl.load_workbook(fn)
ws = wb.active
ws.delete_cols(3,2)
wb.save("out5_11.xlsx")




