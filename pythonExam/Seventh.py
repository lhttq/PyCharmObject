#7．输入10名同学的分数求及格同学的均值，如果分数低于60，则不计入计算中
ls = list(input("请输入10个学生的成绩，用逗号隔开：").split(','))
ls = list(map(float,ls))
ave = 0
print(ls)
for i in ls:
    if i < 60:
        ls.remove(i)
for i in ls:
    ave = ave + i
print(ave/len(ls))
