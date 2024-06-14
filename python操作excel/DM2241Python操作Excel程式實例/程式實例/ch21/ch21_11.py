# ch21_11.py
import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)
df = pd.read_excel("data21_11.xlsx",
                   skiprows=2,usecols="B:H")

print(df['姓名'])
print("-"*70)
print(df[['姓名','部門']])







