#5输入一个由n(n>1)个数字组成的列表ls，并根据该列表输出一个新列表lt，其中lt中第i个元素等于ls中除ls[i]之外所有元素的乘积。
n = input("请以列表格式输入一个列表：\n")
ls = list(n[1:-1].split(",")) #将输入的字符串转化为字符串列表
ls = list(map(int,ls)) #将字符串列表转换为数字列表
lt = []
print(ls)
num = 1
for i in range(len(ls)):
    for j in range(len(ls)):
        num = num * ls[j]
    num = num / ls[i]
    lt.append(num)
    num = 1
print(lt)
