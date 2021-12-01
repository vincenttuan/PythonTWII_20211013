import pandas as pd
print(pd.__version__)
# Series 計算 2
s = pd.Series([1, 2, 3, 4, 5], index=pd.date_range('20211101', periods=5))
print(s)
# 累加 cumsum()
a = s.cumsum()
print(a)
# 累乘 cumprod()
b = s.cumprod()
print(b)
