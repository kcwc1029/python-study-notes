# ch5_8.py
import openpyxl

fn = "data5_8.xlsx"
wb = openpyxl.load_workbook(fn,data_only=True)
ws = wb.active
ws.insert_cols(3,1)
ws['C3'] = '性別'
wb.save("out5_8.xlsx")




