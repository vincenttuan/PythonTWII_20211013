import pandas as pd
import matplotlib.pyplot as plt
# Series 是一個類似陣列的物件(一維陣列)
# 建立 Series 物件: 使用 list
date = pd.date_range('20211101', periods=4)
s = pd.Series([4, 7, -5, 3], index=date)
print(s)
plt.plot(s.index, s.values, '-')
plt.title('my series chart')
plt.xlabel('date')
plt.ylabel('value')
plt.grid(True)  # 格狀
plt.show()