# ch21_2.py
import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)
df = pd.read_excel("customer.xlsx",index_col=0)
print("輸出前 3 筆資料")
print(df.head(3))
print("-"*70)
print("輸出前 5 筆資料")
print(df.head())
print("-"*70)
print("輸出後 5 筆資料")
print(df.tail())






