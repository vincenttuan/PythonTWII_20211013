import pandas as pd
import matplotlib.pyplot as plt
idx = pd.date_range('20211101', periods=5)
s1 = pd.Series([1, 2, 5, 4 ,3], index=idx)
s2 = pd.Series([7, 3, 5, 1 ,9], index=idx)
s3 = pd.Series([6, 10, 2, 4 ,6], index=idx)

dict = {'s1': s1, 's2': s2, 's3': s3 }
df = pd.DataFrame(dict)
print(df)
# 形狀
print('形狀:', df.shape)
print('列數:', df.shape[0])
print('欄數:', df.shape[1])
# 繪圖出三條線
df.plot()
plt.show()