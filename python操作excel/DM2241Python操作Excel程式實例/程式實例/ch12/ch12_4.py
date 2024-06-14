# ch12_4.py
import openpyxl
from openpyxl.worksheet.datavalidation import DataValidation
import datetime

fn = "data12_3.xlsx"
wb = openpyxl.load_workbook(fn)
ws = wb.active
# 建立資料驗證 DataValidation物件
dv = DataValidation(type="date",         
                    operator="lessThan",
                    formula1="TODAY()")
dv.promptTitle = '輸入日期'
dv.prompt = '請輸入到職日期'
dv.errorTitle = "輸入日期錯誤"
dv.error = "不可以輸入未來日期"
dv.add('C4')                    # 設定資料驗證儲存格區間
ws.add_data_validation(dv)      # 將資料驗證加入工作表
# 儲存結果
wb.save('out12_4.xlsx')


