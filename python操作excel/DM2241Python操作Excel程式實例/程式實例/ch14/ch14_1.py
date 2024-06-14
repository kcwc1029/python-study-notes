# ch14_1.py
import openpyxl
from openpyxl.drawing.image import Image

wb = openpyxl.Workbook()
ws = wb.active

img = Image("city.jpg")     # 建立影像物件 img
ws.add_image(img,'A1')      # 將 img 插入 A1
# 儲存結果
wb.save('out14_1.xlsx')


