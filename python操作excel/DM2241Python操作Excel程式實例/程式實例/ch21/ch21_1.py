# ch21_1.py
import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)
df = pd.read_excel("customer.xlsx",index_col=0)
print(df.info())







