import turtle
import time
import random

X_BOUND = 500
Y_BOUND = 500

STEP_SIZE = 5
TURN_SIZE = 5

NumberOfTurtles = 50


screen = turtle.Screen()
turtle.tracer(False)
turtle.screensize(2 * X_BOUND + 10, 2 * Y_BOUND + 10)
screen.listen()

sd_turtles: list[turtle.Turtle] = []
turtles: list[turtle.Turtle] = []

def double_turtles():
    global turtles
    ttm = 2*(len(turtles)) or 1
    for i in range(ttm):
        t = turtle.Turtle()
        t.shape('turtle')
        t.pensize('5')
        turtle.colormode(255)
        t.color((random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))
        x = random.randint(-X_BOUND, X_BOUND)
        y = random.randint(-Y_BOUND, Y_BOUND)
        t.goto(x, y)
        turtles.append(t)
        t.position()
        print(len(turtles))
screen.onkeypress(double_turtles, "r")




def add_turtles():
    global turtles
    for i in range(1):
        t = turtle.Turtle()
        t.shape('turtle')
        t.pensize('5')
        turtle.colormode(255)
        t.color((random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))
        x = random.randint(-X_BOUND, X_BOUND)
        y = random.randint(-Y_BOUND, Y_BOUND)
        t.goto(x, y)
        turtles.append(t)
        t.position()
        print(len(turtles))
screen.onkeypress(add_turtles, "t")




def add_sqaure():
    global turtles
    for i in range(1):
        t = turtle.Turtle()
        t.shape('square')
        t.pensize('15')
        turtle.colormode(255)
        t.color((random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))
        x = random.randint(-X_BOUND, X_BOUND)
        y = random.randint(-Y_BOUND, Y_BOUND)
        t.goto(x, y)
        turtles.append(t)
        t.position()
        print(len(turtles))
screen.onkeypress(add_sqaure, "s")


def add_arrow():
    global turtles
    for i in range(1):
        t = turtle.Turtle()
        turtle.colormode(255)
        t.color((random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))
        x = random.randint(-X_BOUND, X_BOUND)
        y = random.randint(-Y_BOUND, Y_BOUND)
        t.goto(x, y)
        turtles.append(t)
        t.position()
        print(len(turtles))
screen.onkeypress(add_arrow, "a")


def add_circle():
    global turtles
    for i in range(1):
        t = turtle.Turtle()
        t.shape('circle')
        t.pensize('25')
        turtle.colormode(255)
        t.color((random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))
        x = random.randint(-X_BOUND, X_BOUND)
        y = random.randint(-Y_BOUND, Y_BOUND)
        t.goto(x, y)
        turtles.append(t)
        t.position()
        print(len(turtles))
screen.onkeypress(add_circle, "c")

























def draw_square(t):
    for i in range(4):
        t.forward(80)
        t.left(90)


while True:
    for t in sd_turtles:
        draw_square(t)
        (old_x, old_y) = t.possition()
        possilble_moves = [t.forward, t.back, t.right, t.left]
        random_value = random.randint(0, 100)
        random.choice(possilble_moves)(random_value)
        (new_x,new_y) = t.possition()
        if (new_x > X_BOUND or new_x < -X_BOUND or new_y > Y_BOUND or new_y < -Y_BOUND):
            t.goto(old_x, old_y)
    time.sleep(0.5)
    screen.update()



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

def remove_turtle():
    if len(turtles) == 0:
        return
    t = turtles.pop(0)
    t.clear()
    t.hideturtle()
screen.onkeypress(remove_turtle, "-")


while True:
    time.sleep(0.05)
    screen.update()




