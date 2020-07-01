#时间函数
import time as t
t.time()#获取系统时间戳
t.ctime()#获取系统时间(人可读)
他=t.gmtime()#获取系统时间,计算机可读
print(t.ctime())
print(t.gmtime())

