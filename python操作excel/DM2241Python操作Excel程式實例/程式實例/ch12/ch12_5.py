# ch12_5.py
import openpyxl
from openpyxl.worksheet.datavalidation import DataValidation

fn = "data12_5.xlsx"
wb = openpyxl.load_workbook(fn)
ws = wb.active
# 建立 部門 資料驗證 DataValidation物件
dv = DataValidation(type="list",         
                    formula1='"財務,研發,業務"',
                    allow_blank=True)
dv.add('C4:C5')                 # 設定資料驗證儲存格區間
ws.add_data_validation(dv)      # 將資料驗證加入工作表
# 建立 性別 資料驗證 DataValidation物件
dv = DataValidation(type="list",         
                    formula1='"男,女"',
                    allow_blank=True)
dv.add('D4:D5')                 # 設定資料驗證儲存格區間
ws.add_data_validation(dv)      # 將資料驗證加入工作表
# 儲存結果
wb.save('out12_5.xlsx')


