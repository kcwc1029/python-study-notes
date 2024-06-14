# ch8_3.py
import openpyxl
from openpyxl.styles.numbers import is_date_format

print(is_date_format('#,##0.00'))
print(is_date_format('mm-dd-yy'))
print(is_date_format('yy-mm-dd'))
print(is_date_format('d-mm-yy'))





