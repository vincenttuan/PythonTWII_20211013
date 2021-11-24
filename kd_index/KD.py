import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # 顯示所有欄位
    pd.set_option('display.max_columns', None)
    # 顯示所有列
    pd.set_option('display.max_rows', None)
    # 設定列表寬度
    pd.set_option('display.width', 500)
    # 資料庫路徑
    db_path = '../每日股價/財經資料庫.db'
    conn = sqlite3.connect(db_path)
    # 查找某一檔股票(0050)最近幾天(450天)的紀錄
    sql = '''
        SELECT strftime('%Y%m%d', date) as date, 開盤價, 最高價, 最低價, 收盤價 FROM price
        WHERE stock_id = '0050' and 
              strftime('%Y%m%d', date)  in (SELECT DISTINCT(strftime('%Y%m%d', date)) as date FROM price ORDER BY date DESC LIMIT 488)
    '''
    print(sql)
    # 將資料讀進到 DataFrame
    tx = pd.read_sql(sql, conn)
    tx = tx.set_index('date')
    #print(tx)
    print('---------------------------------------------------------------------------')
    # RSV
    # RSV = (今日收盤價 - 最近9天的最低價) / (最近9天的最高價 - 最近9天的最低價)
    # 計算 9 日內的最高成交價
    tx['9dMax'] = tx['最高價'].rolling(9).max()
    # 計算 9 日內的最低成交價
    tx['9dMin'] = tx['最低價'].rolling(9).min()
    # 刪除 NaN 資料列
    tx = tx.dropna()
    #print(tx)
    print('---------------------------------------------------------------------------')
    tx['RSV'] = 0
    tx['RSV'] = 100 * (tx['收盤價'] - tx['9dMin']) / (tx['9dMax'] - tx['9dMin'])
    #print(tx)
    print('---------------------------------------------------------------------------')
    # apply() 的使用
    def add(n):
        return n + 3
    df = pd.DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6]})
    print(df)
    df['new_y'] = df['y'].apply(add)
    print(df)
