#9．使用turtle库，绘制一个太阳花的图形，如下图所示
import turtle as t
t.fillcolor("yellow")
t.pencolor("red")
t.speed(10)
t.begin_fill()
while True:
    t.forward(400)
    t.right(170)
    if abs(t.pos()) < 1:#看画笔是否回到原点，回到原点为真
        break
t.end_fill()