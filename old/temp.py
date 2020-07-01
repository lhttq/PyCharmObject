#temp.py
n = input()
if n[-3:] in ['cal','Cal']:
    j = eval(n[0:-3])*4.186
    print("{:.3f}J".format(j))
elif n[-1] in ['J','j']:
     cal = eval(n[0:-1])/4.186
     print("{:.3f}cal".format(cal))
else:
    print("输入格式错误：")
