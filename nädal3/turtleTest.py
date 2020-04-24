import turtle
import time

box = turtle.Turtle()

box.rt(90)
box.fd(100)
box.right(90)
box.forward(100)
box.right(90)
box.forward(100)
box.right(90)
box.forward(100)
#box.lt()
#box.bk()
turtle.bgcolor("pink")

box.penup()
box.goto(0, 100)
box.pendown()
n = 10
while n <= 50:
    box.circle(n)
    n = n + 10
box.dot(1000)

box.clear()
box.reset()
box.pen(pencolor="blue", fillcolor="green", pensize="10", speed=10)
box.begin_fill()
box.circle(200)
box.end_fill()

time.sleep(5)