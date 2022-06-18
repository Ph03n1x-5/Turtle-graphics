import turtle                                                       # make the turtle graphics system available in Python

turtle.bgcolor("black");                                        # change background color

turtle.speed(0);                                                    #change drawing speed
turtle.pensize(2);                                                 # change the width of the pen / line to 2
turtle.pencolor("indigo");                                     # change pen / line color
#----------------------------------------------------------------------------------------------------------------
def drawcircle(radius):                                         # draw cirle with radius parameter
    for i in range(10):                                             # loop with 10 iterations
        turtle.circle(radius)                                      # draw circle with passed radius value
        radius=radius-4                                            # radius assigned value radius-4
#----------------------------------------------------------------------------------------------------------------
def drawdesign():                                                 # draw design
    for i in range(10):                                             # loop with 10 iterations
        drawcircle(150)                                           # draw circle with 150 radius
        turtle.right(36)                                           # turn cursor 36 degrees right
   
drawdesign();                                                   # completes drawing the design
turtle.hideturtle();                                            # hides the cursor
#----------------------------------------------------------------------------------------------------------------
turtle.penup();                                                 # pen moves up                                                     
turtle.goto(-72, 320);                                      # moves the pen to positions -72 for x axis, 320 for y axis
turtle.pendown();                                             # pen moves down
turtle.write("FLOWER", font = ("Algerian", "30", "bold"));
turtle.penup();                                                 # pen moves up

turtle.done();
#----------------------------------------------------------------------------------------------------------------
# END PROGRAM
