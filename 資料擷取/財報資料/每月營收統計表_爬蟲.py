import requests
import pandas as pd
from io import StringIO

def get_monthly_report(year, month):
    # 組合路徑
    url = 'https://mops.twse.com.tw/nas/t21/sii/t21sc03_%d_%d_0.html' % (year-1911, month)
    # 抓取網頁
    r = requests.get(url)
    # 編碼(如果看不到中文就加入以下編碼: big5 或 utf-8)
    r.encoding = 'big5'
    # 把網頁資料透過 StringIO 包裝成一個檔案給 pandas 讀取
    # 要安裝 lxml 套件
    dfs = pd.read_html(StringIO(r.text))
    # 顯示所有欄
    pd.set_option('display.max_columns', None)
    # 顯示所有列
    pd.set_option('display.max_rows', None)
    # 設定欄寬
    pd.set_option('display.width', 5000)
    '''
    for df in dfs:
        if df.shape[1] == 11:
            print(df.shape)
            print(df)
    轉換
    [df for df in dfs if df.shape[1] == 11]
    '''
    df = pd.concat([df for df in dfs if df.shape[1] == 11])
    print(df)
    #print(dfs)

if __name__ == '__main__':
    year = 2021
    month = 10
    df = get_monthly_report(year, month)
