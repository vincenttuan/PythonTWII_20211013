import pandas as pd
print(pd.__version__)
# Series 計算 4
s = pd.Series([1, 2, 3, 4, 5], index=pd.date_range('20211101', periods=5))
print(s)
# 改變型態
a = s < 3
print(a)
a = a.astype(int)
print(a)
