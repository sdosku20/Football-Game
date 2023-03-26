import turtle
import sound


# Creating windows

def Create_Windows():
    global t
    global w
    global p
    global s
    t= turtle.Turtle()
    p = turtle.Turtle()
    p.ht()
    s = turtle.Turtle()
    s.ht()
    w= turtle.Turtle()
    w.ht()
    w.color("white")
    turtle.tracer(9)
    turtle.bgcolor("black")
    t.color("white")

Create_Windows()

selectA = False
selectB = False

def select_color_A(x,y):
    global selectA
    selectA = True
    p.showturtle()
    p.penup()
    p.shape("turtle")
    p.seth(90)
    p.color("white")
    p.goto(x,y)
    p.pendown()


def select_color_B(x,y):
    global selectB
    selectB = True
    s.showturtle()
    s.penup()
    s.shape("turtle")
    s.seth(90)
    s.color("white")
    s.goto(x,y)
    s.pendown()

def clear():
    t.clear()
    p.clear()
    s.clear()
    p.ht()
    s.ht()
    w.clear()

#Playing Background sound in menu
sound.Menu_Sound()
Sound = True

color_A = "yellow"
color_B = "red"

#Creating buttons (Start, Music [ON, OFF],How to Play?,Quit)
def Buttons(x,y,text,size):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.write(text,align="center" ,font = ("Arial",size,"bold"))
    t.ht()

def Create():
    Buttons(0,150,"START",18)
    Buttons(0,50,"MUSIC",18)
    t.color("yellow")
    Buttons(-25,30,"ON",10)
    t.color("white")
    Buttons(20,30,"OFF",10)
    Buttons(0,-50,"How to play?",18)
    Buttons(0,-150, "QUIT",18)
    Buttons(0,-170, "(double click on quit)",10)

Create()

# Team Colors when you press Start
def Create_color(x,y,color):
        t.pen(pencolor="white", fillcolor=color, pensize=10, speed=9)
        t.penup()
        t.begin_fill()
        t.goto(x,y)
        t.circle(20)
        t.end_fill()
        t.pendown()


# Tutorial Text
def tutorial(text,x,y,size):
        t.penup()
        t.goto(x,y)
        t.pendown()
        t.write(text,align="center" ,font = ("Arial",size,"bold"))


#Check which button has been clicked
def Check(x,y):
    global color_A
    global color_B
    global selectA
    global selectB

    # Click Quit
    if (x>=-45 and x<=45) and (y<=-110 and y>=-155):
        global Sound
        if Sound:
            sound.Click()
        sound.Menu_Play(1)
        turtle.exitonclick()

    # Click How to Play?
    elif (x>=-100 and x<=100) and (y>=-50 and y<=-20):
        if Sound:
            sound.Click()
        t.clear()
        tutorial("There are two teams: Team A and Team B",0,300,22)
        tutorial("To move first row of Team A press 'w' and 's'.",0,200,18)
        tutorial("To move second row of Team A press 'i' and 'k'.",0,150,18)
        tutorial("To move first row of Team B press 'Up' and 'Down'.",0,100,18)
        tutorial("To move second row of Team B press '8' and '2'.",0,50,18)
        tutorial("When the Game Starts: ",0,-100,22)
        tutorial("Press 'P' to Pause or Press 'Q' to Quit",0,-150,18)
        tutorial("<<BACK",-400,-300,18)

        #t.goto(-450,-300)
    elif (x>=-550 and x<=-350) and (y>=-300 and y<=-260):
        if Sound:
            sound.Click()
        clear()
        selectA = False
        selectB = False
        Create()
    elif (x>=-50 and x<=-12) and (y>=25 and y<=55):
        Sound = True
        sound.ON()
        sound.Menu_Play(0)
        t.penup()
        t.color("yellow")
        t.goto(-25,30)
        t.write("ON",align="center" ,font = ("Arial",10,"bold"))
        t.pendown()
        t.penup()
        t.color("white")
        t.goto(20,30)
        t.write("OFF",align="center" ,font = ("Arial",10,"bold"))
        t.pendown()
    elif (x>=0 and x<=50) and (y>=25 and y<=55):
        Sound = False
        sound.Menu_Play(1)
        t.penup()
        t.color("red")
        t.goto(20,30)
        t.write("OFF",align="center" ,font = ("Arial",10,"bold"))
        t.pendown()
        t.penup()
        t.color("white")
        t.goto(-25,30)
        t.write("ON",align="center" ,font = ("Arial",10,"bold"))
        t.pendown()
    elif (x>=-50 and x<=40) and (y>=150 and y<=185):
        if Sound:
            sound.Click()

        t.clear()
        t.penup()
        t.goto(0,320)
        t.pendown()
        t.write("Choose Team Color",align="center",font = ("Arial",18,"bold"))
        t.penup()
        t.goto(0,300)
        t.pendown()
        t.write("(Double click on color)",align="center",font = ("Arial",10,"bold"))
        t.penup()
        t.goto(-250,250)
        t.pendown()
        t.write("Team A",font = ("Arial",14,"bold"))
        t.penup()
        t.goto(150,250)
        t.pendown()
        t.write("Team B",font = ("Arial",14,"bold"))
        t.penup()
        t.goto(-450,-300)
        t.pendown()
        t.write("<<Back",font = ("Arial",18,"bold"))
        t.penup()
        t.goto(350,-300)
        t.pendown()
        t.write("GO>>",font = ("Arial",18,"bold"))

        #Choose Team colors
        Create_color(-220,180,"red")
        Create_color(185,180,"red")

        Create_color(-220,120,"cyan")
        Create_color(185,120,"cyan")

        Create_color(-220,60,"purple")
        Create_color(185,60,"purple")

        Create_color(-220,0,"yellow")
        Create_color(185,0,"yellow")

        Create_color(-220,-60,"blue")
        Create_color(185,-60,"blue")

        Create_color(-220,-120,"#FF1493")
        Create_color(185,-120,"#FF1493")

        Create_color(-220,-180,"orange")
        Create_color(185,-180,"orange")

    # Clicking colors for Team A
    elif (x>=-250 and x<=-195) and (y>=175 and y<=235):
        color_A = "red"
        select_color_A(-220,198)

    elif (x>=-250 and x<=-195) and (y>=115 and y<=165):
        color_A = "cyan"
        select_color_A(-220,138)

    elif (x>=-250 and x<=-195) and (y>=57 and y<=110):
        color_A = "purple"
        select_color_A(-220,78)

    elif (x>=-250 and x<=-195) and (y>=-5 and y<=50):
        color_A = "yellow"
        select_color_A(-220,18)

    elif (x>=-250 and x<=-195) and (y>=-70 and y<=-20):
        color_A = "blue"
        select_color_A(-220,-42)

    elif (x>=-250 and x<=-195) and (y>=-125 and y<=-70):
        color_A = "#FF1493"
        select_color_A(-220,-102)

    elif (x>=-250 and x<=-195) and (y>=-190 and y<=-130):
        color_A = "orange"
        select_color_A(-220,-162)

    # Clicking colors for Team B
    elif (x>=155 and x<=210) and (y>=175 and y<=235):
        color_B = "red"
        select_color_B(185,198)

    elif (x>=155 and x<=210) and (y>=115 and y<=165):
        color_B = "cyan"
        select_color_B(185,138)

    elif (x>=155 and x<=210) and (y>=57 and y<=110):
        color_B = "purple"
        select_color_B(185,78)

    elif (x>=155 and x<=210) and (y>=-5 and y<=50):
        color_B = "yellow"
        select_color_B(185,18)

    elif (x>=155 and x<=210) and (y>=-70 and y<=-20):
        color_B = "blue"
        select_color_B(185,-42)

    elif (x>=155 and x<=210) and (y>=-125 and y<=-70):
        color_B = "#FF1493"
        select_color_B(185,-102)

    elif (x>=155 and x<=210) and (y>=-190 and y<=-130):
        color_B = "orange"
        select_color_B(185,-162)

    elif (x>=340 and x<=425) and (y>=-305 and y<=-260):
        if selectA == False or selectB == False:
            w.clear()
            w.penup()
            w.goto(0,-300)
            w.pendown()
            w.write("\"The game starts when each team has selected a color\"", align = "center",font = ("Arial",15,"bold"))
            w.ht()
            w.penup()
            w.goto(0,-320)
            w.pendown()
            w.write("(MAKE SURE THAT BOTH TEAMS HAVE SELECTED A COLOR)", align = "center",font = ("Arial",12,"bold"))
            w.ht()
        elif color_B == color_A:
            w.clear()
            w.penup()
            w.goto(0,-300)
            w.pendown()
            w.write("\"It's against the rules if both teams have the same color\"", align = "center",font = ("Arial",15,"bold"))
            w.ht()
            w.penup()
            w.goto(0,-320)
            w.pendown()
            w.write("(MAKE SURE THAT BOTH TEAMS HAVE UNIQUE COLOR)", align = "center",font = ("Arial",12,"bold"))
            w.ht()

        else:
            sound.Menu_Play(1)
            clear()
            #starting the game
            import Start





turtle.listen()
turtle.onscreenclick(Check,1)
turtle.done()