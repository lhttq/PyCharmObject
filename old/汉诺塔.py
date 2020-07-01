#汉诺塔
#i = input("请输入圆盘的层数"):
count = 0
def hanol(i,a,b,c):
    global count
    if i==1:
        print("{}:{}->{}".format(1,a,c))
        count += 1
    else:
        hanol(i-1,a,c,b)
        print("{}:{}->{}".format(i,a,c))
        count += 1
        hanol(i-1,c,b,a)
hanol(7,'A','C','B')
print(count)