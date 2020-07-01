#对于一个列表，在保持非零元素相对顺序的同时，将元素中所有的数字0移动到末尾。
n = input("请以列表格式输入一个列表：\n")
ls = list(n[1:-1].split(",")) #将输入的字符串转化为字符串列表
ls = list(map(int,ls)) #将字符串列表转换为数字列表
lt = []
zero = []
for i in ls:
    if i == 0:
        zero.append(i)
    else:
        lt.append(i)
lt.sort()
lt = lt + zero
print(lt)