# Stop Sign
# CS 175
# Therese Racancoj

import turtle


t = turtle.Turtle()
t.shape('turtle')
t.color('red')

t.begin_fill()
for i in range(8):
    t.forward(60)
    t.left(45)
t.end_fill()
t.penup()
t.goto(30, -25)
t.left(90)

t.color('white')
t.penup()
t.goto(-36, 36)
t.write('STOP', font = ('Impact', 50))
t.goto(-38, -20)
