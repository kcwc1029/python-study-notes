# ch7_11.py
import openpyxl
from openpyxl.comments import Comment

wb = openpyxl.Workbook()
ws = wb.active
ws.column_dimensions.group('D','F',hidden=True)
wb.save("out7_11.xlsx")




