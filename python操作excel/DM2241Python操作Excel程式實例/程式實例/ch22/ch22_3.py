# ch22_3.py
import pandas as pd

pd.set_option('display.unicode.east_asian_width',True)
# 讀取銷售資料
df = pd.read_excel("salesReport.xlsx")
# 統計男與女的職業類別數
sex_group = df.groupby(['性別'])
print(sex_group['職業類別'].value_counts())
print("-"*70)
# 統計男與女的購買商品類別數
print(sex_group['商品類別'].value_counts())



