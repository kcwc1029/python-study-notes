# ch12_1.py
import openpyxl
from openpyxl.worksheet.datavalidation import DataValidation

fn = "data12_1.xlsx"
wb = openpyxl.load_workbook(fn)
ws = wb.active
# 建立資料驗證 DataValidation物件
dv = DataValidation(type="whole",         
                    operator="between",
                    formula1=75,
                    formula2=500)
dv.add('D3:D4')                 # 設定資料驗證儲存格區間
ws.add_data_validation(dv)      # 將資料驗證加入工作表
# 儲存結果
wb.save('out12_1.xlsx')


