import turtle #this moves around and draw staff - Introduced to
#help kids learn programming easily

def draw_square():
    window = turtle.Screen()
    window.bgcolor("gray")
    
    brad = turtle.Turtle() # to grab a turtle
    brad.shape("square")
    brad.color("blue")
    brad.speed(1)
    for x in range(0,4):
        brad.forward(100)      # move 100 steps forward
        brad.right(90)         # turn right 90 degrees
    
    window.exitonclick()

draw_square()
