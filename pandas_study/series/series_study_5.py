import pandas as pd
print(pd.__version__)
# Series 計算 3
s = pd.Series([1, 2, 3, 4, 5], index=pd.date_range('20211101', periods=5))
print(s)
# 移動窗格 rolling(n)
a = s.rolling(2).sum()
print(a)
b = s.rolling(3).max()
print(b)
