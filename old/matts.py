#田字格
def matts(n):
    for i in range(n):
        if i%5==0:
            for j in range(n):
                if j%5 == 0 and j == n-1:
                    print("+")
                    continue
                elif j%5 == 0:
                    print("+",end='')
                else:
                    print("-",end='')
        else:
            j = 0
            for j in range(n):
                if j%5 == 0 and j == n-1:
                    print("|")
                    continue
                elif j%5 == 0:
                    print("|",end='')
                else:
                    print(" ",end='')

def main():
    matts(31)
main()

