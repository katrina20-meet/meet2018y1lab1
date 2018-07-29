import turtle

# Everything that comes after the # is a 
# comment.
# It is a note to the person reading the code.
# The computer ignores it.
# Write your code below here...


# ...and end it before the next line.


import turtle

turtle.penup() #Pick up the pen so it doesn’t 
               #draw
turtle.goto(-200,-100) #Move the turtle to the 
 #position (-200, -100) 
 #on the screen
turtle.pendown() #Put the pen down to start
                 #drawing
#Draw the M:
turtle.goto(-200,-100+200) 
turtle.goto(-200+50,-100) 
turtle.goto(-200+100,-100+200)
turtle.goto(-200+100,-100) 
turtle.mainloop

#draw the E:
turtle.penup()
turtle.goto(-200+210,-100+200)
turtle.pendown()
turtle.goto(-200+110,-100+200)
turtle.goto(-200+110,-100)
turtle.goto(-200+210,-100)
turtle.penup()
turtle.goto(-200+110,0)
turtle.pendown()
turtle.goto(-200+210,0)

turtle.penup()
turtle.goto(-200+320,-100+200)
turtle.pendown()
turtle.goto(-200+220,-100+200)
turtle.goto(-200+220,-100)
turtle.goto(-200+320,-100)
turtle.penup()
turtle.goto(-200+220,0)
turtle.pendown()
turtle.goto(-200+320,0)



turtle.mainloop()
