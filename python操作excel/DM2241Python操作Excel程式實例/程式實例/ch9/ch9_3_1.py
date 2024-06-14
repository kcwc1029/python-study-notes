# ch9_3_1.py
import openpyxl

fn = "data9_3.xlsx"
wb = openpyxl.load_workbook(fn)
ws = wb.active
ws.cell(row=7,column=3,value="=SUM(C4:C6)")
wb.save("out9_3_1.xlsx")












