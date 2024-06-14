# ch20_51.py
import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)
x = pd.read_excel("out20_50a.xlsx",index_col=0)
items = ['軟體','書籍','國際證照']
y = pd.read_excel("out20_50b.xlsx",names=items)
print(x)
print("-"*70)
print(y)







