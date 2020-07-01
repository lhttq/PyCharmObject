#货币转换
ymin = input('输入起始年份：')
ymax = input('输入截止年份：')
ymin = eval(ymin)
ymax = eval(ymax)
for i in range(ymin,ymax):
    if i%4.0 == 0 and i%100 != 0 or i%400 == 0:
        print(i)

