# ch7_5.py
import openpyxl

fn = "data7_5.xlsx"
wb = openpyxl.load_workbook(fn)
ws = wb.active
ws.freeze_panes = 'A3'
wb.save("out7_5.xlsx")




