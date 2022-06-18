import turtle # make the turtle graphics system available in Python

turtle.bgcolor("black"); # change background color

turtle.speed(0); #change drawing speed
turtle.pensize(2); # change the width of the pen / line to 2
turtle.pencolor("indigo"); # change pen / line color to "indigo"
#----------------------------------------------------------------------------------------------------------------
def drawcircle(radius):
    for i in range(10):
        turtle.circle(radius)
        radius=radius-4

def drawdesign():
    for i in range(10):
        drawcircle(150)
        turtle.right(36)
        
drawdesign();
turtle.hideturtle();

turtle.penup();
turtle.goto(-72, 320);
turtle.pendown();
turtle.write("FLOWER", font = ("Algerian", "30", "bold"));
turtle.penup();

turtle.done();
#----------------------------------------------------------------------------------------------------------------
# END PROGRAM
