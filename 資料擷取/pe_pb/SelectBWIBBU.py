import sqlite3

conn = sqlite3.connect('../../資料庫/財經資料庫.db')
cursor = conn.cursor()
sql = 'select * from BWIBBU where pe > 0 and pe < 20 and pb < 1 and yield > 10'
cursor.execute(sql)
rows = cursor.fetchall()
for row in rows:
    print(row)