import sqlite3
conn = sqlite3.connect("tw_stock.db")
cursor = conn.cursor()
sql = "insert into portfolio(symbol, cost, amount, ts) " \
      "values(?, ?, ?, ?)"

# 內容一定要是元祖 Tuple
datas = [('2303', 50, 7000, '2021-11-3'),
         ('2317', 110, 6000, '2021-11-3'),
         ('2498', 70.5, 4000, '2021-11-3')]

# 批次新增
cursor.executemany(sql, datas)

conn.commit()
conn.close()
