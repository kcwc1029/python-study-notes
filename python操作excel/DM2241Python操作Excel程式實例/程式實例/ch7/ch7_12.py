# ch7_12.py
import openpyxl
from openpyxl.comments import Comment

wb = openpyxl.Workbook()
ws = wb.active
ws.column_dimensions.group('D','F', hidden=True)
ws.row_dimensions.group(5,10, hidden=True)
wb.save("out7_12.xlsx")




