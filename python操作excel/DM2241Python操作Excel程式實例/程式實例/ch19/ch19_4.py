# ch19_4.py
import csv
import openpyxl

fn = 'csvReport.csv'
with open(fn,encoding='utf-8') as csvFile:  # 開啟csv檔案
    csvReader = csv.reader(csvFile)     # 建立Reader物件
    listReport = list(csvReader)        # 將資料轉成串列
    
wb = openpyxl.Workbook()                # 建立活頁簿
ws = wb.active
ws.append(listReport[0])                # 寫入標題欄
report = listReport[1:]                 # 移除第 0 列的標題欄
for row in report:                      # 迴圈處理串列內容
    row[3] = int(row[3])                # 將索引 3 欄轉成整數
    row[4] = int(row[4])                # 將索引 4 欄轉成整數
    row[5] = int(row[5])                # 將索引 5 欄轉成整數
    ws.append(row)                      # 將串列寫入儲存格
wb.save("out19_4.xlsx") 







