import turtle
import menu

speed = 1
#Coordiantes of Team A (Yellow)
x1 = -350
x2 = 120
Y_A_1 = [200,0,-200]
Y_A_2 = [200,0,-200]

#Coordiantes of Team B (Red)
x3 = -120
x4 = 350
Y_B_1 = [200,0,-200]
Y_B_2 = [200,0,-200]


class Player(turtle.Turtle):
    def __init__(self,x,y,speed):
        turtle.Turtle.__init__(self)
        self.color(menu.color_A)
        self.shape("turtle")
        self.shapesize(2,2,2)
        self.speed = speed
        self.penup()
        self.goto(x,y)

    def rotate(self):
        self.color(menu.color_B)
        self.left(180)


#Players of Team A
player1_A = Player(x1,Y_A_1[0],speed)
player2_A = Player(x1,Y_A_1[1],speed)
player3_A = Player(x1,Y_A_1[2],speed)
player4_A = Player(x2,Y_A_2[0],speed)
player5_A = Player(x2,Y_A_2[1],speed)
player6_A = Player(x2,Y_A_2[2],speed)


#Players of Team B
player1_B = Player(x3,Y_B_1[0],speed)
player1_B.rotate()
player2_B = Player(x3,Y_B_1[1],speed)
player2_B.rotate()
player3_B = Player(x3,Y_B_1[2],speed)
player3_B.rotate()
player4_B = Player(x4,Y_B_2[0],speed)
player4_B.rotate()
player5_B = Player(x4,Y_B_2[1],speed)
player5_B.rotate()
player6_B = Player(x4,Y_B_2[2],speed)
player6_B.rotate()

#Moving Up First column of team A (Yellow)
def moveUp_1_A():
    Y_A_1[0] += 20
    player1_A.sety(Y_A_1[0])
    Y_A_1[1] += 20
    player2_A.sety(Y_A_1[1])
    Y_A_1[2] += 20
    player3_A.sety(Y_A_1[2])

#Moving Down First column of team A (Yellow)
def moveDown_1_A():
    Y_A_1[0] -= 20
    player1_A.sety(Y_A_1[0])
    Y_A_1[1] -= 20
    player2_A.sety(Y_A_1[1])
    Y_A_1[2] -= 20
    player3_A.sety(Y_A_1[2])

#Moving Up Second column of team A (Yellow)
def moveUp_2_A():
    Y_A_2[0] += 20
    player4_A.sety(Y_A_2[0])
    Y_A_2[1] += 20
    player5_A.sety(Y_A_2[1])
    Y_A_2[2] += 20
    player6_A.sety(Y_A_2[2])

#Moving Down Second column of team A (Yellow)
def moveDown_2_A():
    Y_A_2[0] -= 20
    player4_A.sety(Y_A_2[0])
    Y_A_2[1] -= 20
    player5_A.sety(Y_A_2[1])
    Y_A_2[2] -= 20
    player6_A.sety(Y_A_2[2])


#Moving Up or Down First column of team B (Red)

def moveUp_1_B():
    Y_B_1[0] += 20
    player1_B.sety(Y_B_1[0])
    Y_B_1[1] += 20
    player2_B.sety(Y_B_1[1])
    Y_B_1[2] += 20
    player3_B.sety(Y_B_1[2])

def moveDown_1_B():
    Y_B_1[0] -= 20
    player1_B.sety(Y_B_1[0])
    Y_B_1[1] -= 20
    player2_B.sety(Y_B_1[1])
    Y_B_1[2] -= 20
    player3_B.sety(Y_B_1[2])

#Moving Up or Down Second column of team B (Red)

def moveUp_2_B():
    Y_B_2[0] += 20
    player4_B.sety(Y_B_2[0])
    Y_B_2[1] += 20
    player5_B.sety(Y_B_2[1])
    Y_B_2[2] += 20
    player6_B.sety(Y_B_2[2])

def moveDown_2_B():
    Y_B_2[0] -= 20
    player4_B.sety(Y_B_2[0])
    Y_B_2[1] -= 20
    player5_B.sety(Y_B_2[1])
    Y_B_2[2] -= 20
    player6_B.sety(Y_B_2[2])


#Player Collisions up and down

        #Up Collisions
def Player_Collision():
    if Y_A_1[0] > 290:
        Y_A_1[0] = 280
        Y_A_1[1] = 80
        Y_A_1[2] = -120

    if Y_A_2[0] > 280:
        Y_A_2[0] = 280
        Y_A_2[1] = 80
        Y_A_2[2] = -120

    if Y_B_1[0] > 280:
        Y_B_1[0] = 280
        Y_B_1[1] = 80
        Y_B_1[2] = -120

    if Y_B_2[0] > 280:
        Y_B_2[0] = 280
        Y_B_2[1] = 80
        Y_B_2[2] = -120

    #Down Collisions
    if Y_A_1[2] < -280:
        Y_A_1[0] = 120
        Y_A_1[1] = -80
        Y_A_1[2] = -280


    if Y_A_2[2] < -280:
        Y_A_2[0] = 120
        Y_A_2[1] = -80
        Y_A_2[2] = -280

    if Y_B_1[2] < -280:
        Y_B_1[0] = 120
        Y_B_1[1] = -80
        Y_B_1[2] = -280

    if Y_B_2[2] < -280:
        Y_B_2[0] = 120
        Y_B_2[1] = -80
        Y_B_2[2] = -280















