
# coding: utf-8

# ## 【Python提高】时间

# ## 时间格式
# 
# 在Python中，通常有这几种方式来表示时间：1）时间戳； 2）格式化的时间字符串； 3）元组（struct_time）共九个元素。
# 
# 1）时间戳（timestamp）的方式：
# 
# 通常来说，时间戳表示的是从1970年1月1日00:00:00开始按秒计算的偏移量。我们运行“type(time.time())”，返回的是float类型。返回时间戳方式的函数主要有time()，clock()等。
# 
# 2）格式化的时间字符串，比如"%Y-%m-%d %H:%M:%S"
# 
# 3）元组（struct_time）方式：
# 
# struct_time元组共有9个元素，返回struct_time的函数主要有gmtime()，localtime()，strptime()。下面列出这种方式元组中的几个元素：
# 
# struct_time(tm_year=2016, tm_mon=2, tm_mday=2, tm_hour=11, tm_min=16, tm_sec=43, tm_wday=1, tm_yday=33, tm_isdst=0)
# 
# 年，月，日，时，分，秒，星期几（0-6），年的第几天，是否夏令时（默认为-1）
# 
# ### 接着介绍time模块中常用的几个函数：
# 
# 1）time.localtime([secs])：将一个时间戳转换为当前时区的struct_time。secs参数未提供，则以当前时间为准。
# 
# 2）time.gmtime([secs])：和localtime()方法类似，gmtime()方法是将一个时间戳转换为UTC时区（0时区）的struct_time。
# 
# 3）time.time()：返回当前时间的时间戳。
# 
# 4）time.mktime(t)：将一个struct_time转化为时间戳。
# 
# 5）time.sleep(secs)：线程推迟指定的时间运行。单位为秒。
# 
# 6）time.clock()：这个需要注意，在不同的系统上含义不同。在UNIX系统上，它返回的是“进程时间”，它是用秒表示的浮点数（时间戳）。而在WINDOWS中，第一次调用，返回的是进程运行的实际时间。而第二次之后的调用是自第一次调用以后到现在的运行时间。（实际上是以WIN32上QueryPerformanceCounter()为基础，它比毫秒表示更为精确）
# 
# 7）time.asctime([t])：把一个表示时间的元组或者struct_time表示为这种形式：'Sun Jun 20 23:21:05 1993'。如果没有参数，将会将time.localtime()作为参数传入。
# 
# 8）time.ctime([secs])：把一个时间戳（按秒计算的浮点数）转化为time.asctime()的形式。如果参数未给或者为None的时候，将会默认time.time()为参数。它的作用相当于time.asctime(time.localtime(secs))。
# 
# 9）time.strftime(format[, t])：把一个代表时间的元组或者struct_time（如由time.localtime()和time.gmtime()返回）转化为格式化的时间字符串。如果t未指定，将传入time.localtime()。如果元组中任何一个元素越界，ValueError的错误将会被抛出。
# 
# 10）time.strptime(string[, format])：把一个格式化时间字符串转化为struct_time。实际上它和strftime()是逆操作。在这个函数中，format默认为："%a %b %d %H:%M:%S %Y"。
# 
# 最后，对time模块进行一个总结。根据之前描述，在Python中共有三种表达方式：1）timestamp 2）tuple或者struct_time 3）格式化字符串。
# 
# 它们之间的转化如图所示：
# 
# ![time.jpg][1]
# 
#   [1]: https://joinquant-image.b0.upaiyun.com/63401413fb815ddbfa112a11a7109f19

# ## 1、使用datetime模块来获取当前的日期和时间

# In[1]:

import datetime
i = datetime.datetime.now()
print ("当前的日期和时间是 %s" % i)
print ("ISO格式的日期和时间是 %s" % i.isoformat() )
print ("当前的年份是 %s" %i.year)
print ("当前的月份是 %s" %i.month)
print ("当前的日期是  %s" %i.day)
print ("dd/mm/yyyy 格式是  %s/%s/%s" % (i.day, i.month, i.year) )
print ("当前小时是 %s" %i.hour)
print ("当前分钟是 %s" %i.minute)
print ("当前秒是  %s" %i.second)


# ## 2、使用time模块来获取当前的时间和日期

# In[6]:

import time
print (time.strftime("%H:%M:%S"))
## 12 hour format ##
print (time.strftime("%I:%M:%S"))
# 日期
print (time.strftime("%d/%m/%Y"))
print (time.localtime())


# ## 3、获取当前时间并转换为指定日期格式

# In[7]:

import datetime
#获得当前时间
now = datetime.datetime.now() # ->这是时间数组格式
print now
#转换为指定的格式:
otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
print otherStyleTime
print now.strftime("%Y-%m-%d")


# ## 4、字符串格式转化
# 
# 如a = "2013-10-10 23:40:00"，想改为 a = "2013/10/10 23:40:00"
# 
# 方法：先转换为时间数组，然后转换为其他格式

# In[5]:

a = "2013-10-10 23:40:00"
timeArray = time.strptime(a, "%Y-%m-%d %H:%M:%S")
otherStyleTime = time.strftime("%Y/%m/%d %H:%M:%S", timeArray)
otherStyleTime


# ## 5、时间和时间戳之间的相互转化

# In[7]:

#日期到时间戳上的转换：
import datetime
import time
t = datetime.datetime(2014,12, 6, 12, 10, 10)
timestamp = time.mktime(t.timetuple())
print timestamp


# In[8]:

#时间戳到时间日期的转换：
import datetime 
import time
t = time.localtime(timestamp)
timeStr = time.strftime('%Y-%m-%d %H:%M:%S', t)
print timeStr


# ## 6、时间戳转换为指定格式日期
# 
# 利用localtime()转换为时间数组,然后格式化为需要的格式,如：

# In[10]:

timeStamp = 1381419600
timeArray = time.localtime(timeStamp)
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
otherStyleTime


# In[12]:

timeStamp = 1381419600
dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")
otherStyleTime


# ## 7、获得三天前的时间的方法

# In[13]:

import time
import datetime
#先获得时间数组格式的日期
threeDayAgo = (datetime.datetime.now() - datetime.timedelta(days = 3))
#转换为时间戳:
timeStamp = int(time.mktime(threeDayAgo.timetuple()))
#转换为其他字符串格式:
otherStyleTime = threeDayAgo.strftime("%Y-%m-%d %H:%M:%S")
otherStyleTime


# ## 8、给定时间戳,计算该时间的几天前时间

# In[14]:

timeStamp = 1381419600
#先转换为datetime
import datetime
import time
dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
threeDayAgo = dateArray - datetime.timedelta(days = 3)
threeDayAgo


# ## 9、计算昨天和明天的日期

# In[15]:

import datetime #导入日期时间模块
today = datetime.date.today() #获得今天的日期
print today #输出今天日期
yesterday = today - datetime.timedelta(days=1) #用今天日期减掉时间差，参数为1天，获得昨天的日期
print yesterday
tomorrow = today + datetime.timedelta(days=1) #用今天日期加上时间差，参数为1天，获得明天的日期
print tomorrow
print "昨天:%s， 今天:%s， 明天：%s" % (yesterday, today, tomorrow) #字符串拼接在一起输出，这3天的日期


# ## 10、获取历史交易日
# 
# 历史交易日往往因为法定节假日的不固定而导致交易日不固定，给我们的回测带来了很大不便，这里提供一个简单方法，通过获取某只股票历史的交易日获得。

# In[16]:

import time
initial = '2005-01-05'
tradingdays = get_price('000423.XSHE', fields='price', start_date=initial, 
                            end_date=time.strftime('%Y-%m-%d', time.localtime()))
tradingdays.index


# In[17]:

start = '2015-06-01'
end = '2015-08-01'
days = tradingdays[start:end].index
days


# In[ ]:



