import pandas as pd
import matplotlib.pyplot as plt
idx = pd.date_range('20211101', periods=5)
s1 = pd.Series([1, 2, 5, 4 ,3], index=idx)
s2 = pd.Series([7, 3, 5, 1 ,9], index=idx)
s3 = pd.Series([6, 10, 2, 4 ,6], index=idx)

dict = {'s1': s1, 's2': s2, 's3': s3 }
df = pd.DataFrame(dict)
print(df)
# 利用 loc / iloc 查找
a = df.loc['2021-11-3':'2021-11-5', ['s1', 's3']]
print(a)
b = df.iloc[2:4, [0, 2]]  # 2:4 (含2不含4)
print(b)