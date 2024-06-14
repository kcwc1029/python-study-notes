# ch13_2.py
import openpyxl

fn = "data13_1.xlsx"
wb = openpyxl.load_workbook(fn)
ws = wb.active

ws.page_setup.orientation = "landscape"
wb.save("out13_2.xlsx")



