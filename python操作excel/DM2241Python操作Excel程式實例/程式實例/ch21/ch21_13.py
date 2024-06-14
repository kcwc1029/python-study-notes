# ch21_13.py
import pandas as pd
import datetime

pd.set_option('display.unicode.east_asian_width', True)
df = pd.read_excel("data21_11.xlsx",
                   skiprows=2,usecols="B:H")

print(df[df['部門'] == '表演組'])
print("-"*70)
print(df[df['月薪'] > 75000])
print("-"*70)
print(df[df['到職日期'] > datetime.datetime(1993,6,1)])







