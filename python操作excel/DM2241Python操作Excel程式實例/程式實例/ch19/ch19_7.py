# ch19_7.py
import openpyxl
import csv

fn = "out19_4.xlsx"
fout = "out19_7.csv"
wb = openpyxl.load_workbook(fn,data_only=True)            
ws = wb.active   
with open(fout,'w',newline='',encoding="utf-8") as csvOFile:  # 供寫入
    csvWriter = csv.writer(csvOFile)
    for row in ws.rows:
        csvWriter.writerow([cell.value for cell in row])



