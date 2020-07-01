#输入一个整数列表，列表元素为20个，元素之间逗号隔开，编写程序，将前10个元素升序排列，后10个元素降序排列，并输出列表

n = input("请以列表格式输入一个列表：\n")
s = list(n[1:-1].split(",")) #将输入的字符串转化为字符串列表
s = list(map(int,s)) #将字符串列表转换为数字列表
a = s[0:10]
a.sort()
b = s[10:20]
b.sort()
b.reverse()
print(s)
print(a)
print(b)
s = a + b
print(s)
