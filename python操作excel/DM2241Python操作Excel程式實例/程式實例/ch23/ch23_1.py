# ch23_1.py
from win32com.client import DispatchEx

myexcel = "D:\Python_Excel\ch23\data23_1.xlsx"
mypdf = "D:\Python_Excel\ch23\out23_1.pdf"

# 建立COM應用物件
obj = DispatchEx("Excel.Application")
# 讀取Excel文件
books = obj.Workbooks.Open(myexcel,False)
# 將文件轉成PDF
books.ExportAsFixedFormat(0, mypdf)
books.Close(False)  # 關閉
obj.Quit()          # 結束







