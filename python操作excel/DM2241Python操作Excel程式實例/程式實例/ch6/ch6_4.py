# ch6_4.py
import openpyxl
from openpyxl.styles import Border, Side

fn = "data6_4.xlsx"
wb = openpyxl.load_workbook(fn)
ws = wb.active

side = Side(border_style='thin')
borders = Border(left=side,right=side,top=side,bottom=side)
for rows in ws['B2':'C6']:
    for cell in rows:
        cell.border = borders                              
wb.save("out6_4.xlsx")




