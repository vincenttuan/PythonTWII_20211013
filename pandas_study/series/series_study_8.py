import pandas as pd
print(pd.__version__)
# 綜合練習 Series 1
# 請求出 s.rolling(2).sum().cumsum() + 1 找出最大值
s = pd.Series([1, 2, 3, 4, 5], index=pd.date_range('20211101', periods=5))
print(s)
print(s.rolling(2).sum())
print(s.rolling(2).sum().cumsum())
print(s.rolling(2).sum().cumsum() + 1)
print((s.rolling(2).sum().cumsum() + 1).max())
