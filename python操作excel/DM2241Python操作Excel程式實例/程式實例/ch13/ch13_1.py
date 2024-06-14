# ch13_1.py
import openpyxl

fn = "data13_1.xlsx"
wb = openpyxl.load_workbook(fn)
ws = wb.active

ws.print_options.horizontalCentered = True
ws.print_options.verticalCentered = True
wb.save("out13_1.xlsx")



