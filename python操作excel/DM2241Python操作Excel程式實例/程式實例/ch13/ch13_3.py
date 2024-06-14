# ch13_3.py
import openpyxl

fn = "data13_1.xlsx"
wb = openpyxl.load_workbook(fn)
ws = wb.active

ws.page_setup.blackAndWhite = True
wb.save("out13_3.xlsx")



