# ch7_6.py
import openpyxl

fn = "data7_5.xlsx"
wb = openpyxl.load_workbook(fn)
ws = wb.active
ws.freeze_panes = 'B1'
wb.save("out7_6.xlsx")




