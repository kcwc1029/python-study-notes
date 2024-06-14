# ch22_1.py
import pandas as pd

pd.set_option('display.unicode.east_asian_width',True)
# 讀取銷售資料
df = pd.read_excel("salesReport.xlsx")
# 輸出原始資料
print(df)
# 統計客戶數
print("-"*70)
customer_count = df.value_counts("客戶編號")
print(customer_count)



