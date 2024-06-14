# ch21_12.py
import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)
df = pd.read_excel("data21_11.xlsx",
                   skiprows=2,usecols="B:H")

print(df.loc[[2]])
print("-"*70)
print(df.loc[[3, 4, 5]])
print("-"*70)
print(df.iloc[3:6])






