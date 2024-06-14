# ch20_52.py
import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)
x = pd.read_excel("data20_52.xlsx",sheet_name="台北店")
print(x)







