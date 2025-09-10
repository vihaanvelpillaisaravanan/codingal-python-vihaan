import turtle
screen = turtle.Screen()
screen.title("star using turtle")
screen.bgcolor("navy")
screen.setup(600,600)

t = turtle.Turtle()
t.shape("turtle")
t.color("white")
t.pensize(8)
t.speed(1)

t.forward(200)
t.left(120)
t.forward(200)
t.left(120)
t.forward(200)

t.right(150)
t.penup()
t.forward(100)
t.right(90)
t.pendown()

t.forward(200)
t.right(120)
t.forward(200)
t.right(120)
t.forward(200)
t.right(120)

turtle.done()

