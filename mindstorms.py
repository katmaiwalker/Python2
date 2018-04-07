import turtle #this moves around and draw staff - Introduced to
#help kids learn programming easily

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")
    
    brad = turtle.Turtle() # to grab a turtle
    for x in range(0,4):
        brad.forward(100)      # move 100 steps forward
        brad.right(90)         # turn right 90 degrees
    
    window.exitonclick()

draw_square()
