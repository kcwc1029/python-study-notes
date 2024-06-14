# ch8_1.py
import openpyxl
from openpyxl.styles.numbers import builtin_format_code

for i in range(50):
    print(f"i = {i} : {builtin_format_code(i)}")





