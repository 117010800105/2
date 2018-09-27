#e2.1DrawPython.py
from random import*
import turtle
turtle.setup(650, 600, 150, 150)
turtle.penup()
turtle.fd(-86.6)
turtle.pendown()
turtle.pensize(5)
turtle.pencolor("purple")
turtle.seth(30)
for i in range(3):
    turtle.fd(150)
    turtle.left(-120)
turtle.penup()
turtle.home()
turtle.seth(60)
turtle.fd(-86.6)
turtle.pendown()
turtle.left(30)
for i in range(3):
    turtle.fd(150)
    turtle.left(-120)
