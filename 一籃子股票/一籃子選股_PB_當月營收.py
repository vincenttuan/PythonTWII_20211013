import sqlite3
import pandas as pd
import datetime
import matplotlib.pyplot as plt
# 一籃子股票指數:
# 股價淨值比 0.1 < pb < 0.5
# 近三個月營收 > 近一年營收
# 回測驗證
# 計算 ROI 報酬率

if __name__ == '__main__':
    # 這一天需要有交易
    tday = datetime.date(2021, 1, 4)
    conn = sqlite3.connect('../資料庫/財經資料庫.db')
    # 股價 >= 2021, 1, 4
    sql = '''
           SELECT stock_id, date, 收盤價 FROM price
           where date >= '%s'
           ''' % (tday)
    print(sql)
    # date -> index, stock_id -> columns, 收盤價 -> data
    price = pd.read_sql(sql, conn, parse_dates=['date']).pivot(index='date', columns='stock_id')['收盤價']
    print(price)

    # PB 股價淨值比 = 2021, 1, 4
    sql = '''
            SELECT CAST(symbol as varchar(10)) as stock_id, ts as date, pb 
            FROM BWIBBU
            where date == '%s'
          ''' % (tday)

    print(sql)
    pb = pd.read_sql(sql, conn, parse_dates=['date']).pivot(index='date', columns='stock_id')['pb']
    print(pb)

    # 當月營收 < 2021, 1, 4
    sql = '''
            SELECT CAST(stock_id as varchar(10)) as stock_id, date, 當月營收 FROM monthly_report
            where date < '%s'
          ''' % (tday)
    print(sql)
    rev = pd.read_sql(sql, conn, parse_dates=['date']).pivot(index='date', columns='stock_id')['當月營收']
    print(rev)

    # 策略條件
    condition1 = pb.columns[(pb.iloc[0] > 0.1) & (pb.iloc[0] < 0.5)]
    print("condition1:", condition1)  # 印出符合策略1的股票
    condition2 = rev.columns[rev.iloc[-3:].mean() > rev.iloc[-12:].mean()]
    print("condition2:", condition2)  # 近 3 個月月營收 > 近 12 個月月營收
    # condition1 & condition2 (交集)
    cond = condition1.intersection(condition2)
    print("cond:", cond)
