# ch5_13.py
import openpyxl

fn = "data5_12.xlsx"
wb = openpyxl.load_workbook(fn)
ws = wb.active
ws.move_range("A1:H6",rows=2,cols=1,translate=True)
wb.save("out5_13.xlsx")




