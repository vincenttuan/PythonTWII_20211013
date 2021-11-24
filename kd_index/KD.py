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
    print(tx)

