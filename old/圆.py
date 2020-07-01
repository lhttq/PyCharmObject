#圆
import turtle as t
r = 50
for i in range(4):
    t.penup()
    t.goto(0,-r)
    t.pendown()
    t.circle(r)
    r+=50
    
    
