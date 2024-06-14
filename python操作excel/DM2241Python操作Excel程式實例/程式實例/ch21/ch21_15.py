# ch21_15.py
import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)
df = pd.read_excel("data21_15.xlsx",
                   skiprows=2,usecols="B:E")


data1 = df['收縮壓'] > 140
print(data1)
data2 = df['舒張壓'] > 90
print(data2)
df['高血壓'] = data1 & data2
print(df)






