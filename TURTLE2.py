import turtle
turtle.color("cyan", "green")
turtle.bgcolor("black")
turtle.begin_fill()
turtle.speed(0)

colors = ["cyan", "white", "yellow", "green", "orange", "pink", "red", "blue"]
for i in range(100):
    turtle.pencolor(colors[i%8])
    turtle.circle(100)
    turtle.right(5)

turtle.hideturtle()

for j in range(50):
    turtle.right(10)
    turtle.pencolor(colors[j%6])
    for i in range(2):

        turtle.forward(200)
        turtle.right(90)

        turtle.forward(100)
        turtle.right(90)

turtle.end_fill()
turtle.done()
