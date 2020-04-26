import turtle
turtle.setup(width=500, height=500)
t = turtle.Pen()
t.color(0,0,1)
t.pencolor(0,1,0)
t.width(10)
t.speed(0)
t.begin_fill()
for i in range(4):
    t.forward(100)
    t.right(90)
    t.circle(50)
t.end_fill()