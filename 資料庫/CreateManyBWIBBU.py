import 資料擷取.pe_pb.BWIBBU as bwi
import 資料庫.CreateOneBWIBBU as bmibbu
from datetime import date, datetime, timedelta
import time
if __name__ == '__main__':
    today = date.today()
    begin_day = date(2021, 1, 1)
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
        bmibbu.create_table()
        bmibbu.create_record(list)
        time.sleep(7)  # 每一次爬完之後要停7秒