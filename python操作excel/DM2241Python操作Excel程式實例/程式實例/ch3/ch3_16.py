# ch3_16.py
import openpyxl

fn = 'data3_16.xlsx'
wb = openpyxl.load_workbook(fn)
ws = wb.active
print(type(ws.rows))        # 獲得ws.rows資料類型
print(type(ws.columns))     # 獲得ws.columns資料類型

    

