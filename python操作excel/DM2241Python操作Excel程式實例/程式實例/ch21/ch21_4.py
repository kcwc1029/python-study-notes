# ch21_4.py
import pandas as pd

df = pd.read_excel("customer.xlsx",index_col=0)
print("輸出各學歷人數")
print(df['學歷'].value_counts())
print("輸出各學歷占比")
print(df['學歷'].value_counts(normalize=True))






