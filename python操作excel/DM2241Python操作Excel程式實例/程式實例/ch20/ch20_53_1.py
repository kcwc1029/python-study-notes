# ch20_53_1.py
import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)
x = pd.read_excel("data20_52.xlsx",header=3,usecols="B:F")
print(x)







