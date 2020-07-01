#8．从键盘任意输入一个正整数n，编程输出该数0~n-1的累加和。（不引用第三方库）
n = input("请输入任意正整数：")
sum = 0
for i in range(eval(n)):
    sum = sum + i
print(sum)