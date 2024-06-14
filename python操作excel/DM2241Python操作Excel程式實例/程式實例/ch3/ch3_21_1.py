# ch3_21_1.py
import openpyxl

fn = 'data3_16.xlsx'
wb = openpyxl.load_workbook(fn)
ws = wb.active
range = ws['A1':'E9']
for a, b, c, d, e in range:
    print(f"{a.value} {b.value} {c.value} {d.value} {e.value}")










