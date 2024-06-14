# ch21_8.py
import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)
df = pd.read_excel("data21_8.xlsx",skiprows=2,usecols="B:F")
print(df.drop_duplicates())












