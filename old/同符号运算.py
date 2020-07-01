#同符号运算
n = input()
if (eval(n) >= 0)&(eval(n) < 10):
    n1 = abs(eval(n)) + 10
    n2 = -(abs(eval(n)) - 10)
    n3 = abs(eval(n)) * 10
elif eval(n) >= 10:
    n1 = abs(eval(n)) + 10
    n2 = abs(eval(n)) - 10
    n3 = abs(eval(n)) * 10
elif eval(n)<-10:
    n1 = -(abs(eval(n)) + 10)
    n2 = -(abs(eval(n)) - 10)
    n3 = -(abs(eval(n)) * 10)
else:
    n1 = -(abs(eval(n)) + 10)
    n2 = abs(eval(n)) - 10
    n3 = -(abs(eval(n)) * 10)
print(abs(eval(n)),n1,n2,n3)
