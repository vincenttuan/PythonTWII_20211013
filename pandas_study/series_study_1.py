import pandas as pd
import matplotlib.pyplot as plt

# Series 是一個類似陣列的物件(一維陣列)
# 建立 Series 物件: 使用 list
#s = pd.Series([4, 7, -5, 3])  # 預設的 index = 0, 1, 2, 3
#s = pd.Series([4, 7, -5, 3], index=['a', 'b', 'c', 'd'])
date = pd.date_range('20211101', periods=4)
s = pd.Series([4, 7, -5, 3], index=date)
print(s)
print(s[1])
print(s[0:3])
print(s.index.values)
print(s.values)
print(s.loc['20211103'])
print(s.iloc[1])
x = s > 0
print(s.loc[x])
