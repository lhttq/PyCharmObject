#3．托运货物收费是根据货物重量来算的，某托运处的收费标准是：货物重量在50千克（包括）以下的，每千克0.5元，超过50千克部分每千克0.6元，写一程序，输入货物重量，输出收费金额。
def fee():
    weight = input("请输入货物的重量,已千克为单位")
    if eval(weight) <= 50 and eval(weight) >= 0:
        money = eval(weight) * 0.5;
    elif eval(weight) > 50:
        money = 50 * 0.5 + (eval(weight) - 50)*0.6
    else:
        print("您的输入有误,请重新输入")
    print("收取金额为：{}".format(money))
fee()