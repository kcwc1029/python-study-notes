# ch21_3.py
import pandas as pd

df = pd.read_excel("customer.xlsx",index_col=0)
print(f"(列數, 欄數) = {df.shape}")







