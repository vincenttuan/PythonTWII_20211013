import pandas as pd
print(pd.__version__)
# 綜合練習 Series 2
# A 股票 2021-11-01~07 價格 = 10
# A 股票 2021-11-08~10 價格 = 15
# 求 Series
s = pd.Series(10, index=pd.date_range('2021-11-01', periods=10))
print(s)
#s.loc['2021-11-08':'2021-11-10'] += 5
s.loc['2021-11-08':] += 5
#s.loc[:'2021-11-08'] += 5
print(s)
