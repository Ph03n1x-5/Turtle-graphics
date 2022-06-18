import turtle
from turtle import *

# Function to draw boarders
def draw_borders(obj, x, y):
    obj.color("red")
    obj.penup()
    obj.goto(x,y)
    obj.pendown()
    obj.forward(400)
    obj.right(90)
    obj.forward(400)
    obj.right(90)
    obj.forward(400)
    obj.right(90)
    obj.forward(400)

# Function to draw second chess board
def draw_first_board(obj):
    for i in range(8):
        for j in range(8):
            if(i + j) % 2 == 1:
                draw_small_rectangle(obj, i, j)


# Function to draw a small rectangle
def draw_small_rectangle(obj, x ,y):
    obj.color("black")
    obj.penup()
    obj.goto(-400 + x * 50, 150 - y * 50)
    obj.pendown()
    obj.begin_fill()
    obj.forward(50)
    obj.right(90)
    obj.forward(50)
    obj.right(90)
    obj.forward(50)
    obj.right(90)
    obj.forward(50)
    obj.right(90)
    obj.end_fill()



# Function to draw second chess board
def draw_second_board(obj):
    for i in range(8):
        for j in range(8):
            if(i + j) % 2 == 1:
                obj.color("black")
                obj.penup()
                obj.goto(100 + i * 50, 150 - j * 50)
                obj.pendown()
                obj.begin_fill()
                obj.forward(50)
                obj.right(90)
                obj.forward(50)
                obj.right(90)
                obj.forward(50)
                obj.right(90)
                obj.forward(50)
                obj.right(90)
                obj.end_fill()
def main():
    turtle.setup(1000, 600)
    turtle.title("Chess Board")
    turtle.speed(0)
    turtle.hideturtle()
    turtle.color("black")
    turtle.pencolor("black")
    turtle.pensize(5)
    draw_borders(turtle, -450, 200)
    draw_borders(turtle, 50, -200)
    draw_first_board(turtle)
    draw_second_board(turtle)
    turtle.done()
    hideturtle()
    exitonclick()

main()
