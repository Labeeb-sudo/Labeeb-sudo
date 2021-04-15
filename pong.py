import turtle
import winsound

ws = turtle.Screen()
ws.bgcolor("black")
ws.title("Pong")
ws.setup(width=800, height=600)
ws.tracer(1)

# Score
score_a = 0
score_b = 0


# paddle
paddle = turtle.Turtle()
paddle.speed(1)
paddle.shape ("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(-350,0)

# paddle b
paddle_b = turtle.Turtle()
paddle_b.shape("square")
paddle_b.speed(100)
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.shape("square")
ball.speed(0)
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0  Player B: 0", align="center",font=("Courier", 24,"normal"))



# function
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


def paddle_up():
    y = paddle.ycor()
    y += 20
    paddle.sety(y)


def paddle_down():
    y = paddle.ycor()
    y -= 20
    paddle.sety(y)



#   Keyborad Binding
ws.listen()
ws.onkeypress(paddle_up,"w")
ws.onkeypress(paddle_down,"s")
ws.onkeypress(paddle_b_up, "Up")
ws.onkeypress(paddle_b_down, "Down")



# Main GameLoop
while True:
    ws.update()
    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking 
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("swoosh.wav", winsound.SND_ASYNC)

    
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("swoosh.wav", winsound.SND_ASYNC)



    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1  
        score_a += 1   
        pen.clear()
        pen.write("Player 1: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound("swoosh.wav", winsound.SND_ASYNC)


    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player 1: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound("swoosh.wav", winsound.SND_ASYNC)

    # paddle and ball collisions

    if(ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1        

    
    if(ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle.ycor() + 40 and ball.ycor() > paddle.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
 
