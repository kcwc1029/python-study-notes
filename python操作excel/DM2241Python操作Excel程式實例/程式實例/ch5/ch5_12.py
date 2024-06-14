# ch5_12.py
import openpyxl

fn = "data5_12.xlsx"
wb = openpyxl.load_workbook(fn,data_only=True)
ws = wb.active
ws.move_range("A1:H6",rows=2,cols=1)
wb.save("out5_12.xlsx")




