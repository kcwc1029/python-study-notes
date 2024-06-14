# ch21_16.py
import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)
df = pd.read_excel("data21_16.xlsx",
                   skiprows=2,usecols="B:E")

df['總計'] = df['一月'] + df['二月']
df['月平均'] = df['總計'] / 2.0
print(df)






