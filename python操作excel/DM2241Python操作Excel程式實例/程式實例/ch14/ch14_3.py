# ch14_3.py
import openpyxl
from openpyxl.drawing.image import Image

wb = openpyxl.Workbook()
ws = wb.active

img = Image("city.jpg")     # 建立影像物件 img
img.width = 200
img.height = 120
ws.add_image(img,'A1')      # 將 img 插入 A1
# 儲存結果
wb.save('out14_3.xlsx')


