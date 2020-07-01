#凯撒密码
s = input()
for i in range(0,len(s)):
    if s[i] == ' ':
        print(' ',end = "")
    elif s[i] in ['x','y','z']:
        print(chr(ord(s[i])-23),end=' ')
    else:
        print(chr(ord(s[i])+3),end = ' ')
  
