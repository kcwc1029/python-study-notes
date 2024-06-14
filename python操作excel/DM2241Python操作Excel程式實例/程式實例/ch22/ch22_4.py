# ch22_4.py
import pandas as pd

pd.set_option('display.unicode.east_asian_width',True)
# 讀取銷售資料
df = pd.read_excel("salesReport.xlsx")
# 分類統計
job_group = df.groupby(['性別'])
print(job_group['金額'].aggregate(['max','min','mean','median']))
print("-"*70)
job_group = df.groupby(['職業類別'])
print(job_group['金額'].aggregate(['max','min','mean','median']))

