# ch9_9.py
import openpyxl
from openpyxl.formula.translate import Translator

fn = "data9_6.xlsx"
wb = openpyxl.load_workbook(fn)
ws = wb.active

for i in range(4,10):
    index = 'D' + str(i)
    e_index = 'E' + str(i)
    ws[e_index] = "=RANK({},$D$4:$D$9)".format(index)
wb.save("out9_9.xlsx")











