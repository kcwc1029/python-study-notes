# ch21_10.py
import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)
df = pd.read_excel("data21_9.xlsx",
                   skiprows=1,usecols="B:F")
print(df)
print("-"*70)
df.columns = ['姓名','第一季','第二季','第三季','總計']
df.index = [i for i in range(1,6)]
print(df)












