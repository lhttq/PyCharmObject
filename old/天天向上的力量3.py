#天天向上的力量
n = eval(input())
b = 1
a = 1
n1 = pow((b+(n/1000)),365)
n2 = pow((a-(n/1000)),365)
n3 = n1/n2
print("%.2f,%.2f,%d"%(n1,n2,n3))
print("{:.2f},{:.2f},{:.0f}".format(n1,n2,n3))

