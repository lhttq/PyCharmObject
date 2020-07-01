#七段数码管绘制
import turtle as t
import datetime as d
def drawLine(draw):
    t.pendown() if draw else t.penup() #if else 的简写
    t.fd(40) #前进40
    t.right(90)#右转90
def drawDight(dight):
    drawLine(True) if dight in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if dight in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if dight in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if dight in [0,2,6,8] else drawLine(False)
    t.left(90)
    drawLine(True) if dight in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if dight in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if dight in [0,1,2,3,4,7,8,9] else drawLine(False)
    t.left(180)
    t.penup()
    t.fd(20)
def drawDate(date):
    for i in date:
        drawDight(eval(i))
def main():
    t.setup(800,350,200,200)
    t.penup()
    t.fd(-300)
    t.pensize(5)
    drawDate(d.datetime.now().strftime("%Y%m%d"))
    t.hideturtle()
    t.done()
main()
        
