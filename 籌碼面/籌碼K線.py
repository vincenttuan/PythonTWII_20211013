import requests
import re
def get_code(rs):
    headers = {'User-Agent': 'chrome'}
    res = rs.get('http://bsr.twse.com.tw/bshtm/bsMenu.aspx', headers=headers)
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
if __name__ == '__main__':
    rs = requests.session()
    viewstate, eventvalidation = get_code(rs)
    print('viewstate = ' + viewstate)
    print('eventvalidation = ' + eventvalidation)

