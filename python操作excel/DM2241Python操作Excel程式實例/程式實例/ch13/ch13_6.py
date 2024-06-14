# ch13_6.py
import openpyxl

fn = "data13_4.xlsx"
wb = openpyxl.load_workbook(fn)
ws = wb.active

ws.oddFooter.right.text = "&A Page-&P"
ws.oddFooter.right.size = 14
ws.oddFooter.right.font = "Old English Text MT"
ws.oddFooter.right.color = "0000FF"
wb.save("out13_6.xlsx")



