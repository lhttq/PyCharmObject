#进度条
import time as t
scale = 10
print("-------执行开始------")
for i in range(scale+1):
    a = '*' * i
    b = '.' * (scale - i)
    c = (i/scale) * 100
    print("{:^3.3f}%[{}->{}]".format(c,a,b))
    t.sleep(1)
print("-------执行结束-------")
