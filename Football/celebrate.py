import players
import turtle

def Celebrate_TeamA():
    turtle.tracer(5)
    for i in range (288):
        if i<=50 or (i>=100 and i<=150) or (i>=200 and i<=250)  :
            players.player1_A.shapesize(5,5,5)
            players.player2_A.shapesize(5,5,5)
            players.player3_A.shapesize(5,5,5)
            players.player4_A.shapesize(5,5,5)
            players.player5_A.shapesize(5,5,5)
            players.player6_A.shapesize(5,5,5)
        else:
            players.player1_A.shapesize(3,3,3)
            players.player2_A.shapesize(3,3,3)
            players.player3_A.shapesize(3,3,3)
            players.player4_A.shapesize(3,3,3)
            players.player5_A.shapesize(3,3,3)
            players.player6_A.shapesize(3,3,3)

        players.player1_A.right(5)
        players.player2_A.right(5)
        players.player3_A.right(5)
        players.player4_A.right(5)
        players.player5_A.right(5)
        players.player6_A.right(5)


    if i == 288-1:
        turtle.tracer(0)
        players.player1_A.shapesize(2,2,2)
        players.player2_A.shapesize(2,2,2)
        players.player3_A.shapesize(2,2,2)
        players.player4_A.shapesize(2,2,2)
        players.player5_A.shapesize(2,2,2)
        players.player6_A.shapesize(2,2,2)


def Celebrate_TeamB():
    turtle.tracer(5)
    for i in range (288):
        if i<=50 or (i>=100 and i<=150) or (i>=200 and i<=250)  :
            players.player1_B.shapesize(5,5,5)
            players.player2_B.shapesize(5,5,5)
            players.player3_B.shapesize(5,5,5)
            players.player4_B.shapesize(5,5,5)
            players.player5_B.shapesize(5,5,5)
            players.player6_B.shapesize(5,5,5)
        else:
            players.player1_B.shapesize(3,3,3)
            players.player2_B.shapesize(3,3,3)
            players.player3_B.shapesize(3,3,3)
            players.player4_B.shapesize(3,3,3)
            players.player5_B.shapesize(3,3,3)
            players.player6_B.shapesize(3,3,3)

        players.player1_B.right(5)
        players.player2_B.right(5)
        players.player3_B.right(5)
        players.player4_B.right(5)
        players.player5_B.right(5)
        players.player6_B.right(5)


    if i == 288-1:
        turtle.tracer(0)
        players.player1_B.shapesize(2,2,2)
        players.player2_B.shapesize(2,2,2)
        players.player3_B.shapesize(2,2,2)
        players.player4_B.shapesize(2,2,2)
        players.player5_B.shapesize(2,2,2)
        players.player6_B.shapesize(2,2,2)

