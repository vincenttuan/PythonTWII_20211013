import requests

def getData():
    url = 'https://www.twse.com.tw/exchangeReport/BWIBBU_d?response=csv&date=20211103&selectType=ALL'
    data = requests.get(url).text
    data = data.split("\r\n")
    # print(type(data), data)
    list = []  # 用來存放已經整理好的資料
    for d in data:
        d = d.replace('"', '')
        array = d.split(",")
        if len(array) == 8 and array[0] != '證券代號':
            row = (
                    array[0],
                    array[1],
                    float(array[2]) if array[2] != '-' else -1,
                    float(array[4]) if array[4] != '-' else -1,
                    float(array[5]) if array[5] != '-' else -1,
                    '2021-11-03'
                )
            list.append(row)
    return list

if __name__ == '__main__':
    list = getData()
    print(list)
