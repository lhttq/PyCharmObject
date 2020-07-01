n=eval(input())
a=abs(n)
b=a+10
c=a-10
d=a*10
if n>=0:
    print(a,abs(b),abs(c),abs(d))
else: 
    print(a,-abs(b),-abs(c),-abs(d))
