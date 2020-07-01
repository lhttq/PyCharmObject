#星号三角形
n = eval(input())
b = n // 2 + 1
for i in range(b):
    v = n // 2 - i
    print((" " * v) + ("*" * (i * 2 + 1)))
    
