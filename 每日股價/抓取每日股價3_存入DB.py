import requests
import pandas as pd
import io
import sqlite3

date = '2021-11-17'
url = 'https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=%s&type=ALLBUT0999&_=1637142255914' % (date.replace("-", ""))
r = requests.get(url)
lines = r.text.split('\n')
newlines = []
for line in lines:
    if(len(line.split('",')) == 17):
        newlines.append(line)
data = "\n".join(newlines).replace('=', '')
df = pd.read_csv(io.StringIO(data))
df = df.astype(str)
df = df.apply(lambda s: s.str.replace(',', ''))
# 加入日期
df['交易日'] = date
df = df.set_index(['證券代號', '交易日'])
df = df.apply(lambda s: pd.to_numeric(s, errors='coerce'))
df = df.dropna(axis=1, how='all')
print(df)
#-------------------------------------------------------------
# 先存成 csv 再轉存 sqlite
df.to_csv("price.csv", encoding="utf_8")  # utf_8_sig or utf_8
# 轉存 sqlite3
conn = sqlite3.connect('財經資料庫.db')
#df.to_sql('price', conn, if_exists='replace')
df.to_sql('price', conn, if_exists='append')