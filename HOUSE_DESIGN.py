from turtle import *

speed(0)

# Grass
bgcolor("green")

# Sky
penup()
goto(-400, -100)
pendown()
color("deepskyblue")
begin_fill()

for i in range(2) :
    forward(800)
    left(90)
    forward(500)
    left(90)
end_fill()

# Sun
penup()
goto(-320, 225)
pendown()
color("yellow")
begin_fill()
circle(35)
end_fill()

# Cloud
penup()
goto(200, 200)
pendown()
color("white")
begin_fill()
circle(25)
end_fill()

penup()
goto(220, 240)
pendown()
begin_fill()
circle(25)
end_fill()

penup()
goto(230, 215)
pendown()
begin_fill()
circle(25)
end_fill()

penup()
goto(180, 225)
pendown()
begin_fill()
circle(25)
end_fill()

# House
penup()
goto(-100, -100)
pendown()
pensize(3)
color("chocolate", "orange") # (stroke, fill)
begin_fill()

for i in range(4) :
    forward(170)
    left(90)
end_fill()

# Chimney
penup()
goto(20, 130)
pendown()
color("brown", "firebrick")
begin_fill()

for i in range(2) :
    forward(40)
    left(90)
    forward(100)
    left(90)
end_fill()

# Roof
penup()
goto(-127, 70)
pendown()
begin_fill()
for i in range(3) :
    forward(225)
    left(120)
end_fill()

# Window 1
penup()
goto(0, 0)
pendown()
color("black", "white")
begin_fill()

for i in range(4) :
    forward(50)
    left(90)
end_fill()

# Window 1 Cross - Horizontal Line
penup()
goto(0, 25)
pendown()
color("black")
forward(50)

# Windown 1 Cross - Vertical Line
penup()
goto(25, 0)
pendown()
left(90)
forward(50)

# Window 2
penup()
goto(-80, 0)
pendown()
right(90)
color("black", "white")
begin_fill()

for i in range(4) :
    forward(50)
    left(90)
end_fill()

# Window 2 Cross - Horizontal Line
penup()
goto(-80, 25)
pendown()
color("black")
forward(50)

# Windown 2 Cross - Vertical Line
penup()
goto(-55, 0)
pendown()
left(90)
forward(50)

# Door
penup()
goto(-40, -97)
pendown()
right(90)
color("red")
begin_fill()

for i in range(2) :
    forward(50)
    left(90)
    forward(80)
    left(90)
end_fill()

# Door Handle
penup()
goto(-30, -60)
pendown()
color("black")
begin_fill()
circle(5)

# Sidewalk
penup()
goto(-40, -97)
pendown()
color("grey")
begin_fill()

for i in range(2) :
    forward(50)
    right(90)
    forward(160)
    right(90)
end_fill()

# Tree leaf 1
penup()
goto(-200, -50) 
pendown()
color("darkgreen")
begin_fill()
circle(25)
end_fill()

penup()
goto(-220, -90) 
pendown()
begin_fill()
circle(25)
end_fill()

penup()
goto(-230, -65)
pendown()
begin_fill()
circle(25)
end_fill()

penup()
goto(-180, -75)
pendown()
begin_fill()
circle(25)
end_fill()

# Tree trunk 1
penup()
goto(-205, -73)
pendown()
color("brown")
begin_fill()

for i in range(2) :
    forward(15)
    right(90)
    forward(80)
    right(90)
end_fill()

# Tree leaf 2
penup()
goto(-100, -50)
pendown()
color("darkgreen")
begin_fill()
circle(25)
end_fill()

penup()
goto(-120, -90)
pendown()
begin_fill()
circle(25)
end_fill()

penup()
goto(-130, -65)
pendown()
begin_fill()
circle(25)
end_fill()

penup()
goto(-80, -75)
pendown()
begin_fill()
circle(25)
end_fill()

# Tree trunk 2
penup()
goto(-105, -73)
pendown()
color("brown")
begin_fill()

for i in range(2) :
    forward(15)
    right(90)
    forward(80)
    right(90)
end_fill()

# Tree leaf 3
penup()
goto(200, -50)
pendown()
color("darkgreen")
begin_fill()
circle(25)
end_fill()

penup()
goto(180, -90)
pendown()
begin_fill()
circle(25)
end_fill()

penup()
goto(170, -65)
pendown()
begin_fill()
circle(25)
end_fill()

penup()
goto(220, -75)
pendown()
begin_fill()
circle(25)
end_fill()

# Tree trunk 3
penup()
goto(195, -73)
pendown()
color("brown")
begin_fill()

for i in range(2) :
    forward(15)
    right(90)
    forward(80)
    right(90)
end_fill()

# Tree leaf 4
penup()
goto(60, -50)
pendown()
color("darkgreen")
begin_fill()
circle(25)
end_fill()

penup()
goto(40, -90)
pendown()
begin_fill()
circle(25)
end_fill()

penup()
goto(30, -65)
pendown()
begin_fill()
circle(25)
end_fill()

penup()
goto(80, -75)
pendown()
begin_fill()
circle(25)
end_fill()

# Tree trunk 4
penup()
goto(55, -73)
pendown()
color("brown")
begin_fill()

for i in range(2) :
    forward(15)
    right(90)
    forward(80)
    right(90)
end_fill()

# Shrub 1
penup()
goto(60, -250)
pendown()
color("darkgreen")
begin_fill()
circle(25)
end_fill()

penup()
goto(40, -290)
pendown()
begin_fill()
circle(25)
end_fill()

penup()
goto(30, -265)
pendown()
begin_fill()
circle(25)
end_fill()

penup()
goto(80, -275)
pendown()
begin_fill()
circle(25)
end_fill()

# Shrub 2
penup()
goto(-90, -250)
pendown()
color("darkgreen")
begin_fill()
circle(25)
end_fill()

penup()
goto(-110, -290)
pendown()
begin_fill()
circle(25)
end_fill()

penup()
goto(-120, -265)
pendown()
begin_fill()
circle(25)
end_fill()

penup()
goto(-70, -275)
pendown()
begin_fill()
circle(25)
end_fill()

# Car body
color("red")
penup()
goto(30,-300)
pendown()
begin_fill()
forward(370)
left(90)
forward(50)
left(90)
forward(370)
left(90)
forward(50)
end_fill()

# Car windows
penup()
goto(120,-250)
pendown()
setheading(45)
forward(70)
setheading(0)
forward(100)
setheading(-45)
forward(70)
setheading(90)
penup()
goto(220,-250)
pendown()
forward(49.50)

# Car tires
penup()
goto(120,-300)
pendown()
color("black")
begin_fill()
circle(20)
end_fill()
penup()
goto(320,-300)
pendown()
color("black")
begin_fill()
circle(20)
end_fill()

hideturtle()
exitonclick()
