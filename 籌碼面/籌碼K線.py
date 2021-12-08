import time

import pandas as pd
import requests
from io import StringIO
import re
import requests.packages.urllib3

requests.packages.urllib3.disable_warnings()
headers = {'User-Agent': 'chrome'}

# 取得驗證碼
def get_code(rs):
    res = rs.get('http://bsr.twse.com.tw/bshtm/bsMenu.aspx', verify=False, stream=True, headers=headers, timeout=None)
    #print(res.text)
    # 透過 re 正則表示式來抓取
    viewstate = re.search('__VIEWSTATE"\s+value=.*=', res.text)
    #print("viewstate obj: ", viewstate)
    #print("viewstate.group(0): ", viewstate.group(0))
    #print("viewstate value: ", viewstate.group(0)[20:])
    viewstate = viewstate.group(0)[20:]

    eventvalidation = re.search('__EVENTVALIDATION"\s+value=.*\w', res.text)
    #print("eventvalidation obj: ", eventvalidation)
    #print("eventvalidation.group(0): ", eventvalidation.group(0))
    #print("eventvalidation.group(0)[26:]: ", eventvalidation.group(0)[26:])
    eventvalidation = eventvalidation.group(0)[26:]

    return viewstate, eventvalidation

# 傳送資料（表單）
def send_data(rs, stock_id, viewstate, eventvalidation):
    payload = {
        '__EVENTTARGET': '',
        '__EVENTARGUMENT': '',
        '__LASTFOCUS': '',
        '__VIEWSTATE': viewstate,  # encode_viewstate[:-1],
        '__EVENTVALIDATION': eventvalidation,  # encode_eventvalidation[:-1],
        'RadioButton_Normal': 'RadioButton_Normal',
        'TextBox_Stkno': stock_id,
        'CaptchaControl1 ': 'Z67YB',
        'btnOK': '%E6%9F%A5%E8%A9%A2',
    }

    # 模擬按下「查詢」鍵
    rs.post("https://bsr.twse.com.tw/bshtm/bsMenu.aspx", data=payload, headers=headers, stream=True)
    # 停 1 秒
    time.sleep(1)
    res = rs.get('https://bsr.twse.com.tw/bshtm/bsContent.aspx', verify=False, stream=True)
    return res

def parse_data(text):
    lines = text.split('\n')
    lines = [line for line in lines if len(line.split(',')) == 11]
    df = pd.read_csv(StringIO('\n'.join(lines)))
    #print(df)
    # 取 0~4 欄位 序號,券商,價格,買進股數,賣出股數
    one_df = df[df.columns[:5]]  # 取 0~4
    #print(one_df)
    # 取 6~10 欄位 序號,券商,價格,買進股數,賣出股數
    two_df = df[df.columns[6:]]  # 取 6~10
    # 去除 .1 欄位名
    two_df.columns = two_df.columns.str.replace('.1', '', regex=True)
    #print(two_df)
    # 合併 one_df append two_df
    df = one_df.append(two_df)
    df = df.set_index('序號').sort_index().dropna()
    #print(df)
    return df


if __name__ == '__main__':
    symbol = '1101'
    # 顯示所有列
    pd.set_option('display.max_rows', None)

    rs = requests.session()
    viewstate, eventvalidation = get_code(rs)
    print('viewstate = ' + viewstate)
    print('eventvalidation = ' + eventvalidation)

    res = send_data(rs, symbol, viewstate, eventvalidation)
    res.encoding = 'big5'
    open('test.txt', 'w', encoding='utf-8').write(res.text)

    df = parse_data(res.text)
    #print(df)

    # 買進股數與賣出股數 轉為 int
    df['買進股數'] = df['買進股數'].astype('int')
    df['賣出股數'] = df['賣出股數'].astype('int')
    print(df)

    # 券商總買賣
    buy = df['買進股數'].groupby(df['券商']).sum()
    sell = df['賣出股數'].groupby(df['券商']).sum()
    total = buy - sell
    print(total)

    # 主力券商前 15 大
    top_buy = total.nlargest(15)
    print(top_buy)
    top_sell = total.nsmallest(15)
    print(top_sell)
    diff = top_buy.sum() - top_sell.sum()
    print('前 15 大券商主力指標：', diff)

    # 整體買賣家數差（散戶指標）
    diff2 = (total > 0).sum() - (total < 0).sum()
    print('整體買賣家數差（散戶指標）', diff2)

    print('symbol:', symbol)
