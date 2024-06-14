# ch6_10.py
import openpyxl
from openpyxl.styles import Font
from copy import copy

src = Font(name='Arial', size=16)
dst = copy(src)
print(f"src = {src.name}, {src.size}")
print(f"dst = {dst.name}, {dst.size}")


