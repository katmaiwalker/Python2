import turtle #this moves around and draw staff - Introduced to
#help kids learn programming easily

#General function to draw every type of Shape
def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("gray")
    draw_square()
    draw_circle()
    draw_triangle()
    draw_circle_of_squares()
    #draw_multiple_triangles()
    window.exitonclick()

#Function that draws a simple square
def draw_square():  
    brad = turtle.Turtle() # to grab a turtle
    brad.shape("square")
    brad.color("blue")
    brad.speed(1)
    shape_square_sides(brad)

#Function that takes as a param the turthel object and
#shapes the side of a square using a loop
def shape_square_sides(turtle_obj):
    for x in range(0,4):
        turtle_obj.forward(100)      # move 100 steps forward
        turtle_obj.right(90)         # turn right 90 degrees

def shape_triangle_sides(turtle_obj):
    for x in range(0,3):
        turtle_obj.forward(100) 
        turtle_obj.left(120)

#Draw a cirle
def draw_circle():
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("yellow")
    angie.circle(100)
    
#Draw a triangle , 3 iterations
def draw_triangle():
    joe = turtle.Turtle()
    joe.shape("triangle")
    joe.color("white")
    joe.speed(1)
    shape_triangle_sides(joe)
        
#Draw multiples squares that have a common starting point.
#As a final shape you will observe a circle .
#Here there is a inner and outer loop.
def draw_circle_of_squares():
    andrew = turtle.Turtle()
    andrew.shape("square")
    andrew.speed(8)
    for x in range (0,100):
        shape_square_sides(andrew)
        andrew.right(10)

#Check recursive solution        
def draw_multiple_triangles(): 
    jz = turtle.Turtle()
    jz.shape("triangle")
    jz.color("orange")
    jz.speed(1)
    for x in range(1,100):
        for j in range(0,3):
            jz.forward(100*x) 
            jz.left(120)
        jz.right(180)
        for w in range(0,3):
            jz.forward(100*x)
            jz.right(120)
        jz.right(180)
            

draw_shapes()
