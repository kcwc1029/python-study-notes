# ch8_10.py
import openpyxl
import datetime

wb = openpyxl.Workbook()
ws = wb.active
ws.column_dimensions['B'].width = 40
ws['B2'] = datetime.datetime.today()








