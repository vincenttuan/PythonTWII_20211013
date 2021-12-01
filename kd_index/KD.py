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
    db_path = '../資料庫/財經資料庫.db'
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
    # def add(n):
    #     return n + 3
    # df = pd.DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6]})
    # print(df)
    # df['new_y'] = df['y'].apply(add)
    # print(df)
    print('---------------------------------------------------------------------------')
    # 計算 K 值
    # K 是 RSV 和前一日 K 值的加權平均
    # K = 2/3 * (昨日 K 值) + 1/3 * (今日 RSV)
    K = 0
    def KValue(rsv):
        global K
        K = (2/3) * K + (1/3) * rsv
        return K
    tx['K'] = 0
    tx['K'] = tx['RSV'].apply(KValue)
    #print(tx)
    print('---------------------------------------------------------------------------')
    # 計算 D 值
    # D 是 K值 和前一日 D值 的加權平均
    # D = 2/3 * (昨日 D 值) + 1/3 * (今日的 K 值)
    D = 0
    def DValue(k):
        global D
        D = (2/3) * D + (1/3) * k
        return D
    tx['D'] = 0
    tx['D'] = tx['K'].apply(DValue)
    print(tx)
    print('---------------------------------------------------------------------------')
    # 繪圖
    k = tx['K']
    d = tx['D']
    close = tx['收盤價']
    k.plot(label="K", color='orange')
    d.plot(label="D", color='blue')
    close.plot(label="close", color='gray')
    plt.legend()
    plt.show()

