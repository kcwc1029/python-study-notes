# ch21_14.py
import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)
df = pd.read_excel("data21_14.xlsx",
                   skiprows=2,usecols="B:E")

df['增長'] = df['2022年'] > df['2021年']
print(df)






