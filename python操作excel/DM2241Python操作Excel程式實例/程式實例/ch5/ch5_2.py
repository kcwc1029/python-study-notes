# ch5_2.py
import openpyxl

fn = "data5_1.xlsx"
wb = openpyxl.load_workbook(fn,data_only=True)
ws = wb.active

ws.insert_rows(4,1)
ws.insert_rows(6,1)
ws.insert_rows(8)       # 省略amount參數
ws.insert_rows(10)      # 省略amount參數
wb.save("out5_2.xlsx")




