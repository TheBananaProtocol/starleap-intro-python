import turtle
import time
import random

X_BOUND =150
Y_BOUND = 150

STEP_SIZE = 5
TURN_SIZE = 5

NumberOfTurtles = 0

#add turtle imputs
double_turtle = "r"
add_turtle = "t"
add_sqaure = "q"
add_arrow = "o"
add_circle = "c"
add_triangle = "i"
add_blank = "b"
add_clasic = "l"
draw_bound = "/"



#move imputs
turtles_forward = "w"
turtle_turn_right = "d"
turtle_turn_left = "a"



screen = turtle.Screen()
turtle.tracer(False)
turtle.screensize(2 * X_BOUND + 10, 2 * Y_BOUND + 10)
screen.listen()

sd_turtles: list[turtle.Turtle] = []
turtles: list[turtle.Turtle] = []


#DOUBLE THE TUTLES
def double_turtles():
    global turtles
    ttm = 2*(len(turtles)) or 1
    for i in range(ttm):
        t = turtle.Turtle()
        t.shape('turtle')
        t.pensize('5')
        t.penup()
        t.left(random.randint(1, 360))
        turtle.colormode(255)
        t.color((random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))
        x = random.randint(-X_BOUND, X_BOUND)
        y = random.randint(-Y_BOUND, Y_BOUND)
        t.goto(x, y)
        turtles.append(t)
        t.position()
        print(len(turtles))
screen.onkeypress(double_turtles, double_turtle)



#TURTLE
def add_turtles():
    global turtles
    for i in range(1):
        t = turtle.Turtle()
        t.shape('turtle')
        t.pensize(random.randint(1, 15))
        t.left(random.randint(1, 360))
        t.speed(random.randint(0, 10))
        turtle.colormode(255)
        t.penup()
        t.color((random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))
        x = random.randint(-X_BOUND, X_BOUND)
        y = random.randint(-Y_BOUND, Y_BOUND)
        t.goto(x, y)
        turtles.append(t)
        t.position()
    print(len(turtles))
screen.onkeypress(add_turtles, add_turtle)



#SQAURE TURTLE
def add_sqaures():
    global turtles
    for i in range(50):
        t = turtle.Turtle()
        t.shape('square')
        t.pensize('5')
        t.penup()
        turtle.colormode(255)
        t.color((random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))
        x = random.randint(-X_BOUND, X_BOUND)
        y = random.randint(-Y_BOUND, Y_BOUND)
        t.goto(x, y)
        turtles.append(t)
        t.position()
        print(len(turtles))
screen.onkeypress(add_sqaures, add_sqaure)


#RAAOW TURTLE
def add_arrows():
    global turtles
    for i in range(1):
        t = turtle.Turtle()
        t.penup()
        turtle.colormode(255)
        t.color((random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))
        x = random.randint(-X_BOUND, X_BOUND)
        y = random.randint(-Y_BOUND, Y_BOUND)
        t.goto(x, y)
        turtles.append(t)
        t.position()
        print(len(turtles))
screen.onkeypress(add_arrows, add_arrow)

#circle
def add_circles():
    global turtles
    for i in range(1):
        t = turtle.Turtle()
        t.shape('circle')
        t.pensize('5')
        t.penup()
        turtle.colormode(255)
        t.color((random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))
        x = random.randint(-X_BOUND, X_BOUND)
        y = random.randint(-Y_BOUND, Y_BOUND)
        t.goto(x, y)
        turtles.append(t)
        t.position()
        print(len(turtles))
screen.onkeypress(add_circles, add_circle)


#triangle turtle
def add_triangles():
    global turtles
    for i in range(1):
        t = turtle.Turtle()
        t.shape('triangle')
        t.pensize('5')
        t.penup()
        turtle.colormode(255)
        t.color((random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))
        x = random.randint(-X_BOUND, X_BOUND)
        y = random.randint(-Y_BOUND, Y_BOUND)
        t.goto(x, y)
        turtles.append(t)
        t.position()
        print(len(turtles))
screen.onkeypress(add_triangles, add_triangle)








#blank turtle
def add_blanks():
    global turtles
    for i in range(1):
        t = turtle.Turtle()
        t.shape('blank')
        t.pensize('5')
        t.penup()
        turtle.colormode(255)
        t.color((random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))
        x = random.randint(-X_BOUND, X_BOUND)
        y = random.randint(-Y_BOUND, Y_BOUND)
        t.goto(x, y)
        turtles.append(t)
        t.position()
        print(len(turtles))
screen.onkeypress(add_blanks, add_blank)

#classic turtle
def add_clasics():
    global turtles
    for i in range(1):
        t = turtle.Turtle()
        t.shape('classic')
        t.pensize('5')
        t.penup()
        turtle.colormode(255)
        t.color((random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))
        x = random.randint(-X_BOUND, X_BOUND)
        y = random.randint(-Y_BOUND, Y_BOUND)
        t.goto(x, y)
        turtles.append(t)
        t.position()
        print(len(turtles))
screen.onkeypress(add_clasics, add_clasic)

def draw_bounds():
    t = turtle.Turtle()
    t.pensize('5')
    turtle.colormode(255)
    t.color((random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))
    t.teleport(X_BOUND,Y_BOUND)
    t.goto(X_BOUND,-Y_BOUND)
    t.goto(-X_BOUND,-Y_BOUND)
    t.goto(-X_BOUND,Y_BOUND)
    t.goto(X_BOUND,Y_BOUND)
    t.shape('blank')
screen.onkeypress(draw_bounds, draw_bound)



def check_turtle_location(t):
    if t.xcor() >= X_BOUND:
        return False

    elif t.ycor() >= Y_BOUND:
        return False
    

#turtle move forward
def turtles_forwards_march():
    for t in turtles:
        t.speed(random.randint(1, 60))
        t.forward(5)


        
screen.onkeypress(turtles_forwards_march, turtles_forward)


def turtle_turn_rights():
    for t in turtles:
        t.right(5)
screen.onkeypress(turtle_turn_rights,turtle_turn_right)


def turtle_turn_lefts():
    for t in turtles:
        t.speed(0)
        t.left(5)
screen.onkeypress(turtle_turn_lefts,turtle_turn_left)








def draw_square(t):
    for i in range(4):
        t.forward(80)
        t.left(90)


def fwd():
    for t in turtles:
        t.fd(STEP_SIZE)
screen.onkeypress(fwd, "Up")

def lt():
    for t in turtles:
        t.lt(TURN_SIZE)
screen.onkeypress(lt, "Left")

def rt():
    for t in turtles:
        t.rt(TURN_SIZE)
screen.onkeypress(rt, "Right")







#def remove_turtle():
#    if len(turtles) == 0:
#    return
#    t = turtles.pop(0)
#    t.clear()
#    t.hideturtle()
#screen.onkeypress(remove_turtle, "-")





while True:
    time.sleep(0.05)
    screen.update()




