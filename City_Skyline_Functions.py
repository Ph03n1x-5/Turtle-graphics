from turtle import *

bgcolor("black")


# base
color("dark grey")

# first function
def draw(x,y):
    penup()
    goto(x,y)
    pendown()
    
# second function
def move(length1,angle1,length2,angle2):
    forward(length1)
    right(angle1)
    forward(length2)
    left(angle2)
    

draw(-200,-110)
begin_fill()
forward(410)
right(90)
forward(100)
right(90)
forward(410)
right(90)
forward(100)
end_fill()
penup

# first building(left)
color("grey")
begin_fill()
move(40,90,10,90)
forward(20)
right(90)
move(30,90,10,90)
move(10,90,10,90)
forward(10)

# second building
left(90)
forward(20)
right(90)
move(20,90,20,90)
forward(10)
left(90)

# third building
forward(30)
right(90)
forward(4)
circle(3)
move(4,90,4,90)



# fourth building
move(5,90,2,90)
forward(5)
left(90)
move(7,90,10,90)
move(10,90,6,90)
move(20,90,3,90)
move(10,90,3,90)
forward(5)
right(90)
move(10,90,5,90)
move(3,90,10,90)
move(3,90,20,90)
move(6,90,20,90)
move(3,90,5,90)
move(4,90,8,90)

# between buildings 1

forward(7)
left(90)
move(9,90,10,90)


# fifth building

move(10,90,10,90)
move(100,90,5,90)
move(20,90,5,90)
move(15,90,2,90)
move(10,90,10,90)


# top of fifth building

move(10,90,20,95)
move(90,190,89,95)
move(20,90,10,90)
move(10,90,10,90)
move(2,90,15,90)
move(5,90,20,90)
move(5,90,142,90)

# between buildings 2
forward(4)
left(90)
forward(90)
right(90)
move(50,90,4,90)
forward(6)
right(90)
goto(125,-20)

# sixth building
left(90)
forward(20)
left(90)
move(12,90,4,90)
forward(12)
right(90)
forward(4)
goto(160,30)
left(88)
forward(20)
left(183)
forward(20)
goto(160,30)
left(0)
forward(25)
left(90)
move(4,90,12,90)
move(4,90,15,90)
move(4,90,60,90)
forward(4)
left(90)
forward(40)
right(90)
move(10,90,10,90)
forward(15)
right(90)
forward(60)
end_fill()

# stars
penup()
goto(200, 300)
turns = 5
begin_fill()
color("white")

while turns > 0 :
    forward(25)
    left(145)
    turns = turns - 1
end_fill()

penup()
goto(100, 275)
turns = 5
begin_fill()
color("white")

while turns > 0 :
    forward(25)
    left(145)
    turns = turns - 1
end_fill()

penup()
goto(0, 315)
turns = 5
begin_fill()
color("white")

while turns > 0 :
    forward(25)
    left(145)
    turns = turns - 1
end_fill()

penup()
goto(-100, 265)
turns = 5
begin_fill()
color("white")

while turns > 0 :
    forward(25)
    left(145)
    turns = turns - 1
end_fill()

penup()
goto(-200, 320)
turns = 5
begin_fill()
color("white")

while turns > 0 :
    forward(25)
    left(145)
    turns = turns - 1
end_fill()

hideturtle()
