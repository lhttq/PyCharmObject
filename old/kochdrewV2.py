#KochDrawV2.py
import turtle
def koch(size,n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0,60,-120,60]:
            turtle.left(angle)
            koch(size/3,n-1)
def main():
    turtle.speed(1000)
    turtle.setup(800.400)
    turtle.penup()
    turtle.goto(-300,100)
    turtle.pendown()
    turtle.pensize(2)
    koch(400,4)
    turtle.right(120)
    koch(400,4)
    turtle.right(120)
    koch(400,4)
    turtle.hideturtle()
main()
