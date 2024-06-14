# ch14_5.py
import openpyxl
from openpyxl.drawing.image import Image

fn = "data14_5.xlsx"
wb = openpyxl.load_workbook(fn)
ws = wb.active

img = Image("hung.png")     # 建立影像物件 img
img.width = 64 * 2          # 預留影像寬度
img.height = 23 * 5         # 預留影像高度
ws.add_image(img,'B4')      # 將 img 插入 B4
# 儲存結果
wb.save('out14_5.xlsx')


