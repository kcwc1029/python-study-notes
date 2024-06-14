# ch21_20.py
import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)
# 讀取員工資料
left = pd.read_excel("data21_20a.xlsx",
                     skiprows=1,usecols="B:E")
# 讀取員工業績
right = pd.read_excel("data21_20b.xlsx",
                      skiprows=1,usecols="B:C")
df = pd.merge(left,right,left_on='員工ID',right_on='業績ID')    
print("員工資料")
print(left)
print("-"*70)
print("業績表")
print(right)
print("-"*70)
print("合併結果")
print(df)





