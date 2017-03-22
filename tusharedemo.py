# -*- coding: UTF-8 -*-
import tushare, time
from sqlalchemy import create_engine
import datetime
import shares

def get_share_code(str):
    return  str[-7:-1]

now = datetime.datetime.now()
for key in shares.test:
    try:
        print("获取：",key)
        df = tushare.get_k_data(code=get_share_code(key), start='2016-01-28', end = now.strftime('%Y-%m-%d'),pause=0.001)
        engine = create_engine('mysql://root:yb198697@127.0.0.1:3306/shares?charset=utf8')
        # if_exists based on tables ,not data
        df.to_sql('k_day',engine,if_exists='append')
        print("完成：", key)
    except:
        print(key,"获取数据失败")


# for key in shares.all:
#     try:
#         print("获取：",key)
#         df = tushare.get_k_data(code=get_share_code(key), start='2016-01-28', end = now.strftime('%Y-%m-%d'),ktype='60',pause=0.001)
#         engine = create_engine('mysql://root:yb198697@127.0.0.1:3306/shares?charset=utf8')
#         df.to_sql('k_60M',engine,if_exists='append')
#         print("完成：", key)
#     except:
#         print(key,"获取数据失败")

