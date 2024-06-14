# ch1_2.py
import openpyxl

fn = 'sales.xlsx'
wb = openpyxl.load_workbook(fn)     # wb是Excel檔案物件    
print("所有工作表     = ", wb.sheetnames)
print("目前工作表     = ", wb.active)
print("目前工作表名稱 = ", wb.active.title)






