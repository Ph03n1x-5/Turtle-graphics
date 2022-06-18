import turtle                                           # make the turle graphics system available in Python
turtle.speed(10);                                      # changes drawing speed
turtle.bgcolor("navy blue");                     # changes background color
turtle.pensize(5);                                    # changes width of pen / line to 5
turtle.color("blue");                                # changes color to "blue"
turtle.penup();                                         # pen moves up
turtle.goto(-110, -25);                             # moves the pen to positions -110 for x axis, -25 for y axis
turtle.pendown();                                    # moves pen down
turtle.circle(45);                                    # draw circle with 45 radius
turtle.color("black");                              # changes color to "black"
turtle.penup();                                         # pen moves up
turtle.goto(0, -25);                                 # moves the pen to positions 0 for x axis, -25 for y axis
turtle.pendown();                                     # pen moves down
turtle.circle(45);                                     # draw circle with 45 radius
turtle.color("red");                                  # changes color to "red"
turtle.penup();                                         # pen moves up
turtle.goto(110, -25);                               # moves the pen to positions 110 for x axis, -25 for y axis
turtle.pendown();                                     # pen moves down
turtle.circle(45);                                     # draw circle with 45 radius
turtle.color("yellow");                              # changes color to "yellow"
turtle.penup();                                          # pen moves up
turtle.goto(-55, -75);                                # moves the pen to positions -55 for x axis, -75 for y axis
turtle.pendown();                                       # pen moves down
turtle.circle(45);                                       # draw circle with 45 radius
turtle.color("green");                                 # changes color to "green"
turtle.penup();                                           # pen moves up
turtle.goto(55, -75);                                   # moves the pen to positions 55 for x axis, -75 for y axis
turtle.pendown();                                        # pen moves down
turtle.circle(45);                                        # draw circle with 45 radius
#----------------------------------------------------------------------------------------------------------------
# display text "RINGS" in blue circle shape
turtle.penup(); # pen moves up 
turtle.goto(85, 5);  #pen moves to the positions 85 for x axis, 5 for y axis
turtle.pencolor("white"); # moves the pen to positions 85 for x axis, 5 for y axis turtle. pencolor ("white);
turtle.write("RINGS", font = ("Times New Romans", "14", "bold")) #turtle.write("RINGS", font = ("Times New Romans", "14", "bold"))
# display text "RINGS" in black circle shape 
turtle.penup(); # pen moves up 
turtle.goto(-135, 5);  #pen moves to the positions -135 for x axis, 5 for y axis
turtle.pencolor("white"); # moves the pen to positions -135 for x axis, 5 for y axis turtle. pencolor ("white");
turtle.write("RINGS", font = ("Times New Romans", "14", "bold")) #turtle.write("RINGS", font = ("Times New Romans", "14", "bold"))
# display text "RINGS" in red circle shape
turtle.penup(); # pen moves up 
turtle.goto(-25, 5);  #pen moves to the positions -25 for x axis, 5 for y axis
turtle.pencolor("white"); # moves the pen to positions -25 for x axis, 5 for y axis turtle. pencolor ("white");
turtle.write("RINGS", font = ("Times New Romans", "14", "bold")) #turtle.write("RINGS", font = ("Times New Romans", "14", "bold"))
# display text "RINGS" in yellow circle shape
turtle.penup(); # pen moves up 
turtle.goto(-80, -45);  #pen moves to the positions -80 for x axis, -45 for y axis
turtle.pencolor("white"); # moves the pen to positions -80 for x axis, -45 for y axis turtle. pencolor ("white");
turtle.write("RINGS", font = ("Times New Romans", "14", "bold")) #turtle.write("RINGS", font = ("Times New Romans", "14", "bold"))
# display text "RINGS" in green circle shape
turtle.penup(); # pen moves up 
turtle.goto(30, -45);  #pen moves to the positions 30 for x axis, -45 for y axis
turtle.pencolor("white"); # moves the pen to positions 30 for x axis, -45 for y axis turtle. pencolor ("white");
turtle.write("RINGS", font = ("Times New Romans", "14", "bold")) #turtle.write("RINGS", font = ("Times New Romans", "14", "bold"))

turtle.done();
#----------------------------------------------------------------------------------------------------------------
# END PROGRAM
