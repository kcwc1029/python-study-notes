# ch21_6.py
import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)
df = pd.read_excel("data21_5.xlsx",skiprows=2,usecols="B:F")
df1 = df.fillna(0.0)
print(df1)
df1.to_excel(excel_writer="out21_6.xlsx",index=False)











