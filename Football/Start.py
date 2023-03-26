import turtle
import pitch
import players
import ball
import score
import sound
import time
import pygame
import menu

stop = False
is_paused = False

def toogle():
    global is_paused
    if is_paused == True:
        is_paused = False
    else:
        is_paused = True

def Quit():
    global stop
    stop = True


#Keyboard Bindings
turtle.listen()
turtle.onkey(toogle,'p')

# Quit the Game
turtle.onkey(Quit,'q')

#Move Team A
turtle.onkey(players.moveUp_1_A,'w')
turtle.onkey(players.moveDown_1_A,'s')
turtle.onkey(players.moveUp_2_A,'i')
turtle.onkey(players.moveDown_2_A,'k')

#Move Team B
turtle.onkey(players.moveUp_1_B,'Up')
turtle.onkey(players.moveDown_1_B,'Down')
turtle.onkey(players.moveUp_2_B,'8')
turtle.onkey(players.moveDown_2_B,'2')

if menu.Sound == True:
    sound.Background_Sound()
    sound.Whistle()

start = time.time()
time.sleep(0.01)

# Gameloop
while stop == False:
    if not is_paused:
        turtle.clear()
        duration = time.time() - start
        if duration > 200:
            stop = True
            exit()

        #Move the Ball
        ball.ball.penup()
        ball.ball.setx(ball.ball.xcor() + ball.ball.dx)
        ball.ball.sety(ball.ball.ycor() + ball.ball.dy)
        ball.ball.pendown()
        #Check for collisions
        ball.check()
        players.Player_Collision()
    else:
        #Pause the game
        start = time.time()
        turtle.color("#6500DF")
        turtle.write("Game is PAUSED", align = 'center', font = ("Arial",12,"bold"))
        turtle.ht()

    turtle.update()

#Making sure that the right name of the winner will be printed
if menu.color_A == "#FF1493":
    menu.color_A = "pink"
elif menu.color_B == "#FF1493":
    menu.color_B = "pink"

#Stopping the background song
if menu.Sound == True:
    sound.Background_Play(1)
    sound.End_Whistle()
# Printing The Winner Team or Tie
turtle.color("#0E07FA")
if score.score_A  > score.score_B:
    turtle.write(menu.color_A.upper() + " Team Won!", align = 'center', font = ("Arial",28,"bold"))
elif score.score_A  < score.score_B:
    turtle.write(menu.color_B.upper() + " Team Won!", align = 'center', font = ("Arial",28,"bold"))
else:
    turtle.write("Tie!", align = 'center', font = ("Arial",28,"bold"))
turtle.ht()

turtle.done()