# ch21_17.py
import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)
df = pd.read_excel("data21_17.xlsx",
                   skiprows=2,usecols="B:E")

df = df.sort_values(by='銷售數量',ascending=False)
rank = range(1,7)
df['排名'] = rank
print(df)
print("-"*70)
df = df.sort_index()
print(df)





