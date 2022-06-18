import turtle
from turtle import *

bgcolor("white")

# 1. Function to draw borders
def draw_borders(turtle_obj, x, y):
    turtle_obj.color("red")
    turtle_obj.penup()
    turtle_obj.goto(x, y)
    turtle_obj.pendown()
    turtle_obj.forward(400)
    turtle_obj.right(90)
    turtle_obj.forward(400)
    turtle_obj.right(90)
    turtle_obj.forward(400)
    turtle_obj.right(90)
    turtle_obj.forward(400)

# 2. Function to draw Second Chess Board
def draw_first_chess_board(turtle_obj):
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 1:
                draw_small_rectangle(turtle_obj, i, j)

# a. Function to draw A Small Rectangle
def draw_small_rectangle(turtle_obj, x, y):
    turtle_obj.color("black")
    turtle_obj.penup()
    turtle_obj.goto(-400+x*50, 150-y*50)
    turtle_obj.pendown()
    turtle_obj.begin_fill()
    turtle_obj.forward(50)
    turtle_obj.right(90)
    turtle_obj.forward(50)
    turtle_obj.right(90)
    turtle_obj.forward(50)
    turtle_obj.right(90)
    turtle_obj.forward(50)
    turtle_obj.right(90)
    turtle_obj.end_fill()

# 3. Function to draw Second Chess Board
def draw_second_chess_board(turtle_obj):
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 1:
                turtle_obj.color("black")
                turtle_obj.penup()
                turtle_obj.goto(100+i*50, 150-j*50)
                turtle_obj.pendown()
                turtle_obj.begin_fill()
                turtle_obj.forward(50)
                turtle_obj.right(90)
                turtle_obj.forward(50)
                turtle_obj.right(90)
                turtle_obj.forward(50)
                turtle_obj.right(90)
                turtle_obj.forward(50)
                turtle_obj.right(90)
                turtle_obj.end_fill()

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
    draw_first_chess_board(turtle)
    draw_second_chess_board(turtle)
    turtle.done()
    hideturtle()
    exitonclick()

main()


