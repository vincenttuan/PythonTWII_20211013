import 資料擷取.pe_pb.BWIBBU as bwi
import sqlite3
import time
import requests
from datetime import date, datetime, timedelta
import time

def create_table():
    sql = '''
        create table if not exists BWIBBU(
            id integer primary key not null,
            symbol varchar(20) not null,
            name varchar(20) not null,
            yield float not null,
            pe float not null,
            pb float not null,
            ts date 
          ) 
    '''
    conn = sqlite3.connect('../../資料庫/財經資料庫.db')
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()

def create_record(list):
    sql = "insert into BWIBBU(symbol, name, yield, pe, pb, ts) values(?, ?, ?, ?, ?, ?)"
    conn = sqlite3.connect('../../資料庫/財經資料庫.db')
    cursor = conn.cursor()
    cursor.executemany(sql, list)
    conn.commit()
    conn.close()
    print('OK')

if __name__ == '__main__':
    today = date.today()
    begin_day = date(2021, 11, 30)
    print(today, begin_day)
    diff = today - begin_day
    print('diff:', diff)
    for single_date in (begin_day + timedelta(n) for n in range(diff.days+1)):
        print(single_date.strftime("%Y"), single_date.strftime("%m"), single_date.strftime("%d"))
        yyyy = single_date.strftime("%Y")
        mm = single_date.strftime("%m")
        dd = single_date.strftime("%d")
        list = bwi.getData(yyyy, mm, dd)
        print(len(list), list)
        create_table()
        create_record(list)
        time.sleep(7)  # 每一次爬完之後要停7秒
