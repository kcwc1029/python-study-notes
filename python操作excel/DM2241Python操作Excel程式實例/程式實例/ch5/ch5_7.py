# ch5_7.py
import openpyxl

fn = "data5_1.xlsx"
wb = openpyxl.load_workbook(fn,data_only=True)
ws = wb.active
ws.delete_rows(1,ws.max_row)
wb.save("out5_7.xlsx")




