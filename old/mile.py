#单位转换
m = input("请按照xxm或xxin的形式输出")
if m[-1] in ['M','m']:
    In = eval(m[0:-1])*39.37
    print("{:.3f}in".format(In))
elif m[-2:] in ['in','In']:
    M = eval(m[0:-2])/39.37
    print("{:.3f}m".format(M))
else:
    print("你的输入有误，请重新输入：")
