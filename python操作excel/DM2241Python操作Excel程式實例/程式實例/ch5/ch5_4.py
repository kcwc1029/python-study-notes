# ch5_4.py
import openpyxl

fn = "data5_1.xlsx"
wb = openpyxl.load_workbook(fn,data_only=True)
ws = wb.active
data = ["員工編號","姓名","底薪","獎金","加班費",
        "健保費","勞保費","薪資金額"]
length = len(data)
row = 0;
for i in range(4,8):
    ws.insert_rows(i+row,2)
    for j in range(0, length):    # 寫入薪資項目 
        ws.cell(row=i+row+1,column=j+1,value=data[j])
    row = row + 2
wb.save("out5_4.xlsx")




