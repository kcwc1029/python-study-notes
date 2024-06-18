# ch9_6.py
import openpyxl

fn = "data9_6.xlsx"
wb = openpyxl.load_workbook(fn)
ws = wb.active
ws['E4'] = "=RANK(D4,$D$4:$D$9)"
wb.save("out9_6.xlsx")











