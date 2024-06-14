# ch10_1.py
import openpyxl
from openpyxl.formatting.rule import ColorScaleRule

fn = "data10_1.xlsx"
wb = openpyxl.load_workbook(fn)
ws = wb.active
 
#使用 2 種色階
ws.conditional_formatting.add('G2:G10',
    ColorScaleRule(start_type='min', start_color='FFA500',
                   end_type='max',end_color='00FF00'))
                             
#使用 3 種色階
ws.conditional_formatting.add('B2:F10',
    ColorScaleRule(start_type='min',start_value=None,start_color='FF0000',
                   mid_type='percentile',mid_value=50,mid_color='FFFF00',
                   end_type='max',end_value=None,end_color='00FF00'))

wb.save('out10_1.xlsx')


