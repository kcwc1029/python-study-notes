# ch21_7.py
import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)
df = pd.read_excel("data21_5.xlsx",skiprows=2,usecols="B:F")
print(df.dropna())












