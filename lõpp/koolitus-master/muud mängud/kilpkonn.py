import turtle
import time

box = turtle.Turtle()

turtle.bgcolor("pink")

box.right(90)       # right = rt
box.forward(100)    #forward = ft
box.right(90)       #left = lt
box.forward(100)    #backward = bk    
box.right(90)
box.forward(100)
box.right(90)
box.forward(100)

box.penup()
box.goto(-50, -100)
box.pendown()
#box.circle(500)
n = 10
while n <= 50:
    box.circle(n)
    n = n + 10

box.penup()
box.goto(-50, 0)
box.pendown()
box.dot(10)

box.clear()
box.reset()
box.pen(pencolor="white", fillcolor="orange", pensize="12", speed=10)
box.begin_fill()
box.circle(200)
box.end_fill()

time.sleep(2)

