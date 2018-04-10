import turtle #this moves around and draw staff - Introduced to
#help kids learn programming easily

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("gray")
    draw_square()
    draw_circle()
    draw_triangle()
    window.exitonclick()

def draw_square():  
    brad = turtle.Turtle() # to grab a turtle
    brad.shape("square")
    brad.color("blue")
    brad.speed(1)
    for x in range(0,4):
        brad.forward(100)      # move 100 steps forward
        brad.right(90)         # turn right 90 degrees


def draw_circle():
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("yellow")
    angie.circle(100)

def draw_triangle():
    joe = turtle.Turtle()
    joe.shape("triangle")
    joe.color("white")
    joe.speed(1)
    for x in range(0,3):
        joe.forward(100) 
        joe.left(120)

draw_shapes()
