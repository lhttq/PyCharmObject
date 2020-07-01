#平方加字符串格式化
n = input()
m = pow(eval(n),2)
if len('m') <= 20:
    print("{0:-^20}".format(m))
else:
    print(m)
