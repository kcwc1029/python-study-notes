# ch6_9_1.py
import openpyxl
from openpyxl.styles import Alignment

fn = "data6_9_1.xlsx"
wb = openpyxl.load_workbook(fn)
ws = wb.active
ws.column_dimensions['A'].width = 20
ws.row_dimensions[1].height = 40
ws['A1'].alignment = Alignment(horizontal='center',
                           vertical='center')
wb.save("out6_9_1.xlsx")











