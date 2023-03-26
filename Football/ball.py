import turtle
import players
import score
import sound
import celebrate
import menu

# Setting up Ball
ball = turtle.Turtle()
screen = turtle.Screen()
image = "ball.gif"

# Adding Ball image
screen.addshape(image)
ball.shape(image)
turtle.ht()

#Ball movement
ball.dx = 2
ball.dy = -2


#Border Collisions
def check():

    # Ball Up Collisions
    if ball.ycor() > 280:
        ball.sety(280)
        if menu.Sound == True:
            sound.Ball_Kick()
        ball.clear()
        ball.dy *= -1

    #Ball Down Collisions
    if ball.ycor() < -280:
        ball.sety(-280)
        if menu.Sound == True:
            sound.Ball_Kick()
        ball.clear()
        ball.dy *= -1

    # Ball Left Collisions
    if ball.xcor() <= -580 and (ball.ycor()<=-100 or ball.ycor()>=80):
        ball.setx(-580)
        if menu.Sound == True:
            sound.Ball_Kick()
        ball.clear()
        ball.dx *= -1

    # Ball Right Collisions
    if ball.xcor() >= 580 and (ball.ycor()<=-100 or ball.ycor()>=80):
        ball.setx(580)
        if menu.Sound == True:
            sound.Ball_Kick()
        ball.clear()
        ball.dx *= -1

    # Goal for Team A
    if ball.xcor() >= 580 and (ball.ycor()>=-100 and ball.ycor()<=80):
        score.Add_Score(1)
        if menu.Sound == True:
            sound.Background_Play(1)
            sound.Song_TeamB()
        celebrate.Celebrate_TeamA()
        ball.penup()
        ball.goto(0,0)
        if menu.Sound == True:
            sound.Whistle()
            sound.Background_Play(0)
        ball.dx *= -1
        ball.pendown()

    # Goal for Team B
    if ball.xcor() <= -580 and (ball.ycor()>=-100 and ball.ycor()<=80):
        score.Add_Score(2)
        if menu.Sound == True:
            sound.Background_Play(1)
            sound.Song_TeamA()
        celebrate.Celebrate_TeamB()
        ball.penup()
        ball.goto(0,0)
        if menu.Sound == True:
            sound.Whistle()
            sound.Background_Play(0)
        ball.dx *= -1
        ball.pendown()


    #Player Collisions of Team A with Ball
    if (ball.xcor() < players.player1_A.xcor() + 21 and ball.xcor() > players.player1_A.xcor() - 21) and (ball.ycor() < players.Y_A_1[0] + 21 and ball.ycor() > players.Y_A_1[0] - 21):
        if menu.Sound == True:
            sound.Ball_Kick()
        ball.dx *=-1


    if (ball.xcor() <players.player2_A.xcor() + 21 and ball.xcor() > players.player2_A.xcor() - 21) and (ball.ycor() < players.Y_A_1[1] + 21 and ball.ycor() > players.Y_A_1[1] - 21):
        if menu.Sound == True:
            sound.Ball_Kick()
        ball.dx *=-1


    if (ball.xcor() < players.player3_A.xcor() + 21 and ball.xcor() > players.player3_A.xcor() - 21) and (ball.ycor() < players.Y_A_1[2] + 21 and ball.ycor() > players.Y_A_1[2] - 21):
        if menu.Sound == True:
            sound.Ball_Kick()
        ball.dx *=-1


    if (ball.xcor() < players.player4_A.xcor() + 21 and ball.xcor() > players.player4_A.xcor() - 21) and (ball.ycor() < players.Y_A_2[0] + 21 and ball.ycor() > players.Y_A_2[0] - 21):
        if menu.Sound == True:
            sound.Ball_Kick()
        ball.dx *=-1

    if (ball.xcor() < players.player5_A.xcor() + 21 and ball.xcor() > players.player5_A.xcor() - 21) and (ball.ycor() < players.Y_A_2[1] + 21 and ball.ycor() > players.Y_A_2[1] - 21):
        if menu.Sound == True:
            sound.Ball_Kick()
        ball.dx *=-1

    if (ball.xcor() < players.player6_A.xcor() + 21 and ball.xcor() > players.player6_A.xcor() - 21) and (ball.ycor() < players.Y_A_2[2] + 21 and ball.ycor() > players.Y_A_2[2] - 21):
        if menu.Sound == True:
            sound.Ball_Kick()
        ball.dx *=-1



    #Player Collisions of Team B with Ball
    if (ball.xcor() < players.player1_B.xcor() + 21 and ball.xcor() > players.player1_B.xcor() - 21) and (ball.ycor() < players.Y_B_1[0] + 21 and ball.ycor() > players.Y_B_1[0] - 21):
        if menu.Sound == True:
            sound.Ball_Kick()
        ball.dx *=-1


    if (ball.xcor() < players.player2_B.xcor() + 21 and ball.xcor() > players.player2_B.xcor() - 21) and (ball.ycor() < players.Y_B_1[1] + 21 and ball.ycor() > players.Y_B_1[1] - 21):
        if menu.Sound == True:
            sound.Ball_Kick()
        ball.dx *=-1


    if (ball.xcor() < players.player3_B.xcor() + 21 and ball.xcor() > players.player3_B.xcor() - 21) and (ball.ycor() < players.Y_B_1[2] + 21 and ball.ycor() > players.Y_B_1[2] - 21):
        if menu.Sound == True:
            sound.Ball_Kick()
        ball.dx *=-1


    if (ball.xcor() < players.player4_B.xcor() + 21 and ball.xcor() > players.player4_B.xcor() - 21) and (ball.ycor() < players.Y_B_2[0] + 21 and ball.ycor() > players.Y_B_2[0] - 21):
        if menu.Sound == True:
            sound.Ball_Kick()
        ball.dx *=-1

    if (ball.xcor() < players.player5_B.xcor() + 21 and ball.xcor() > players.player5_B.xcor() - 21) and (ball.ycor() < players.Y_B_2[1] + 21 and ball.ycor() > players.Y_B_2[1] - 21):
        if menu.Sound == True:
            sound.Ball_Kick()
        ball.dx *=-1

    if (ball.xcor() < players.player6_B.xcor() + 21 and ball.xcor() > players.player6_B.xcor() - 21) and (ball.ycor() < players.Y_B_2[2] + 21 and ball.ycor() > players.Y_B_2[2] - 21):
        if menu.Sound == True:
            sound.Ball_Kick()
        ball.dx *=-1



