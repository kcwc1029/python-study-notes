# ch5_14.py
import openpyxl

fn = "data5_14.xlsx"
wb = openpyxl.load_workbook(fn)
ws = wb.active
ws.column_dimensions['A'].width = 20
ws.row_dimensions[1].height = 40
wb.save("out5_14.xlsx")











