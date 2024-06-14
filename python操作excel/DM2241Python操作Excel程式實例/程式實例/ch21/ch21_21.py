# ch21_21.py
import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)
# 讀取總公司員工資料
left = pd.read_excel("data21_21a.xlsx",
                     skiprows=1,usecols="B:E")
# 讀取分公司員工資料
right = pd.read_excel("data21_21b.xlsx",
                      skiprows=1,usecols="B:E")
df = left.merge(right,how='outer')    
print("總公司員工資料")
print(left)
print("-"*70)
print("分公司員工資料")
print(right)
print("-"*70)
print("合併結果")
print(df)





