import turtle

t = turtle.Turtle()

color = ["blue","red","black","violet","purple","brown","yellow","pink","gray","cyan","orange","magenta"]

# Setting up screen and background color
def ScreenSetup():
    WIDTH = 1280
    HEIGHT = 720
    turtle.setup(WIDTH, HEIGHT)
    turtle.title("Table Football")
    turtle.bgcolor("#08F71D")
    turtle.tracer(0)

ScreenSetup()


# White lanes along the pitch
def Square():
    t.penup()
    t.pen(pencolor="#FFFFFF", fillcolor="#08F71D", pensize=10, speed=0)
    t.goto(-580, -300)
    t.pendown()

    for i in range (4):
        if(i%2==0):
            t.forward(1160)
        else:
            t.forward(610)

        t.left(90)

Square()

def Center():
    t.penup()
    t.pen(pencolor="#FFFFFF", fillcolor="#FFFFFF", pensize=10, speed=0)
    t.goto(0,-300)
    t.pendown()
    t.left(90)
    t.forward(610)
    t.penup()
    t.goto(40,0)
    t.pendown()
    t.circle(40)

Center()

def Left_Net():
    t.penup()
    t.goto(-580, -100)
    t.pendown()
    t.right(90)
    t.forward(120)
    t.left(90)
    t.forward(180)
    t.left(90)
    t.forward(120)

Left_Net()

def Right_Net():
    t.penup()
    t.goto(580, -100)
    t.pendown()
    t.forward(120)
    t.right(90)
    t.forward(180)
    t.right(90)
    t.forward(120)

Right_Net()

def Fans():
    t.penup()
    t.goto(-610, -330)
    t.pendown()
    for i in range (4):
        if(i%2==0):
            a=102
        else:
            a=55.5
        Loop(a)
        t.left(90)

def Loop(a):
    for i in range(12):
        t.pencolor(color[i])
        t.forward(a)


Fans()
t.ht()
