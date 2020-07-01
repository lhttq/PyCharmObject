#数据处理
def getNum():       #获取用户不定长输入
    nums = []
    iNumStr = input("请输入数字，按回车键退出:")
    while iNumStr != "":
        nums.append(eval(iNumStr))
        iNumStr = input("请输入数字，按回车推出")
    return nums
def mean(numbers):
    s = 0.0
    for num in numbers:
        s += num
    return s/len(numbers)
def dev(numbers,mean):
    v = 0.0
    for num in numbers:
        v += (num - mean)**2
    return pow(v/len(numbers),0.5)
def median(numbers):
    sorted(numbers)
    size = len(numbers)
    if size % 2 == 0:
        med = (numbers[size//2-1] + numbers[size//2])/2
    else:
        med = numbers[size//2]
    return med
n = getNum()
m = mean(n)
print("平均值:{},方差:{:.2},中位数:{}".format(m,dev(n,m),median(n)))
