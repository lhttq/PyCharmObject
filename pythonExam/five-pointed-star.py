#2．使用turtle库绘制一个红色五角星图形，如下图所示：
import turtle as t
t.fillcolor("red")
t.begin_fill()
while True:
    t.forward(200)
    t.right(144)
    if abs(t.pos()) < 1:#看画笔是否回到原点，回到原点为真
        break
t.end_fill()