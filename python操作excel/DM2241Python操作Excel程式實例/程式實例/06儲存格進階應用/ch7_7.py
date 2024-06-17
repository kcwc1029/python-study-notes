# ch7_7.py
import openpyxl

fn = "data7_5.xlsx"
wb = openpyxl.load_workbook(fn)
ws = wb.active
ws.freeze_panes = 'B3'
wb.save("out7_7.xlsx")




