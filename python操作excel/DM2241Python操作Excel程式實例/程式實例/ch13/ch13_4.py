# ch13_4.py
import openpyxl

fn = "data13_4.xlsx"
wb = openpyxl.load_workbook(fn)
ws = wb.active

ws.print_area = "A4:E9"
wb.save("out13_4.xlsx")



