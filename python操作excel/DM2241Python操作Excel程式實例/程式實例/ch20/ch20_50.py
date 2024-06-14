# ch20_50.py
import pandas as pd

items = ['軟體','書籍','國際證照']
Jan = [200, 150, 80]
Feb = [220, 180, 100]
March = [160, 200, 110]
April = [100, 120, 150]
df = pd.DataFrame([Jan, Feb, March, April],
                  columns = items,
                  index = range(1,5))
df.to_excel("out20_50a.xlsx")
df.to_excel("out20_50b.xlsx", header=False, index=False)









