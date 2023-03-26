import turtle
import menu

p1 = turtle.Turtle()
p2 = turtle.Turtle()
w = turtle.Turtle()

counter = turtle.Turtle()
screen = turtle.Screen()
image = "scoreboard.gif"

screen.addshape(image)
counter.shape(image)
counter.penup()
counter.goto(530,280)
counter.pendown()

w.penup()
w.goto(530,235)
w.color("white")
w.write("Table Football",align="center",font = ("Arial",13,"bold"))
w.ht()

score_A = 0
score_B = 0

p1.pen(pencolor="white", fillcolor="#FFFFFF", pensize=1, speed=0)
p2.pen(pencolor="white", fillcolor="#FFFFFF", pensize=1, speed=0)



def Show_Score():
    p1.clear()
    p2.clear()
    if score_A < 10:
        p1.penup()
        p1.goto(490,260)
        p1.pendown()
    else:
        p1.penup()
        p1.goto(480,260)
        p1.pendown()

    if score_B < 10:
        p2.penup()
        p2.goto(550,260)
        p2.pendown()
    else:
        p2.penup()
        p2.goto(540,260)
        p2.pendown()

    p1.color(menu.color_A)
    p2.color(menu.color_B)
    p1.write(score_A,font = ("Arial",28,"bold"))
    p2.write(score_B,font = ("Arial",28,"bold"))

Show_Score()


def Add_Score(a):
    global score_A
    global score_B
    if a == 1:
        score_A += 1
    else:
        score_B += 1
    Show_Score()


p1.ht()
p2.ht()
turtle.ht()