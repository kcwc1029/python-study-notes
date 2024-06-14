# ch21_18.py
import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)
df = pd.read_excel("data21_18.xlsx",
                   skiprows=2,usecols="B:D")

df['累計來客數'] = df['來客數'].cumsum()
print(df)





