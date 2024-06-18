# ch9_3.py
import openpyxl

fn = "data9_3.xlsx"
wb = openpyxl.load_workbook(fn)
ws = wb.active
ws['C7'] = "=SUM(C4:C6)"
wb.save("out9_3.xlsx")












