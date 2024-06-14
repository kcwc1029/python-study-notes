# ch13_5.py
import openpyxl

fn = "data13_4.xlsx"
wb = openpyxl.load_workbook(fn)
ws = wb.active

ws.oddHeader.left.text = "Page &[Page] of &N"
ws.oddHeader.left.size = 14
ws.oddHeader.left.font = "Old English Text MT"
ws.oddHeader.left.color = "0000FF"
wb.save("out13_5.xlsx")



