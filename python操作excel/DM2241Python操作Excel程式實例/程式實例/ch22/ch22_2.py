# ch22_2.py
import pandas as pd

pd.set_option('display.unicode.east_asian_width',True)
# 讀取銷售資料
df = pd.read_excel("salesReport.xlsx")
# 統計客戶性別
sex_count = df.value_counts("性別")
print(sex_count)
print("-"*70)
# 統計客戶職業類別
job_count = df.value_counts("職業類別")
print(job_count)
print("-"*70)
# 統計商品類別
product_count = df.value_counts("商品類別")
print(product_count)



