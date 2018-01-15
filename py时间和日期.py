# -*- coding: UTF-8 -*-
import time;  # 引入time模块
ticks = time.time()
print "当前时间戳为:", ticks

print '--------------------------------------------------'
# 获取当前时间
import time
localtime = time.localtime(time.time())
print "本地时间为 :", localtime

print '--------------------------------------------------'
# 获取格式化的时间
locatetime = time.asctime(time.localtime(time.time()))
print '本地时间为',locatetime

print '--------------------------------------------------'
# 格式化日期     用time模块的strftime方法来格式化日期
print time.strftime("%Y-%m-%d %H-%M-%S",time.localtime())
print time.strftime("%A %B %d %H:%M:%S",time.localtime())
# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))

print '--------------------------------------------------'
# 获取某月日历
import calendar
cal=calendar.month(2018,1)
print cal

print '--------------------------------------------------'
# Python time sleep() 函数推迟调用线程的运行，可通过参数secs指秒数，表示进程挂起的时间。
print 'start time:',time.ctime()
time.sleep(5)       # 推迟5秒
print 'end time:',time.ctime()

print '--------------------------------------------------'


