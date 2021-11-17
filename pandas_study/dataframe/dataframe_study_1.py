'''
資料類型 - DataFrame
DataFrame就像是我們在使用的excel表格一樣，是一個二維的數據有index和column，
可以透過index和column來找到我們要的某一筆資料。
'''
import pandas as pd
data = {
    'name':['Bob', 'John', 'Mary', 'Helen', 'Jo', 'Jack', None],
    'birth':[2000, 2001, None, 2000, 2001, 2001, 2003],
    'score':[80, None, 100, 100, 90, 80, 70]
}
print(data)
myframe = pd.DataFrame(data)
print(myframe)

myframe = myframe.dropna()  # 將有 None 或 NaN 的資料去除
print(myframe)
