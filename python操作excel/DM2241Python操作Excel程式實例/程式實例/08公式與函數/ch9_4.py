# ch9_4.py
import openpyxl

fn = "data9_3.xlsx"
wb = openpyxl.load_workbook(fn)
ws = wb.active
ws['C7'] = "=C4+C5+C6"
wb.save("out9_4.xlsx")












