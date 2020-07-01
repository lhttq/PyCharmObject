#IBM
def guojiIBM(b):
    if b < 18.5:
        nat = "偏瘦"
    elif 18.5 < b <= 24:
        nat = "正常"
    elif 24< b <= 28:
        nat = "偏胖"
    else:
        nat = "肥胖"
    return nat
def guoninIBM(b):
    if b < 18.5:
        nat = "偏瘦"
    elif 18.5 < b <= 25:
        nat = "正常"
    elif 25< b <=28:
        nat = "偏胖"
    else:
        nat = "肥胖"
    return nat
def main():
    height,width = eval(input("请输入身高和体重，用逗号隔开"))
    b = width / pow(height, 2)
    print("BM的值为：{:.2f}".format(b))
    print("BMI的国际指标：{0}".format(guojiIBM(b)))
    print("BMI的国内指标：{0}".format(guoninIBM(b)))
main()
