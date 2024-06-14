# ch3_17.py
import openpyxl

fn = 'data3_16.xlsx'
wb = openpyxl.load_workbook(fn)
ws = wb.active                               
for cell in list(ws.columns)[0]:    # A欄
    print(cell.value)
for cell in list(ws.rows)[2]:       # 索引是2
    print(cell.value, end=' ')    


