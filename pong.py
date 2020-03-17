import turtle
import winsound


wn = turtle.Screen()
wn.title('Pong BY Umang')
wn.bgcolor('Black')
wn.setup(width=800, height=600)
wn.tracer(0)
score_a = 0
score_b = 0

#PADDLE A
paddle_a = turtle.Turtle()
paddle_a.shape("square")
paddle_a.speed(0)
paddle_a.color('White')
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#PADDLE B
paddle_b = turtle.Turtle()
paddle_b.shape("square")
paddle_b.speed(0)
paddle_b.color('White')
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#BALL
ball = turtle.Turtle()
ball.shape("square")
ball.speed(0)
ball.color('White')
ball.shapesize(stretch_wid=1,stretch_len=1)
ball.penup()
ball.goto(0,0)
ball.dx = 0.2
ball.dy = 0.2

#PEN
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.color("White")
pen.hideturtle()
pen.goto(0,230)
pen.write("Player A: 0 , Player B: 0",align="center",font=("Courier",20,"normal"))

#Paddle A UP
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

#Paddle B UP
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

#Paddle A DOWN
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

#Paddle A DOWN
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#Keyboard Binding
wn.listen()
wn.onkeypress(paddle_a_up,'w')
wn.onkeypress(paddle_b_up,'Up')
wn.onkeypress(paddle_a_down,'s')
wn.onkeypress(paddle_b_down,'Down')

# MAIN LOOP
while True:
    wn.update()

    #Move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Board Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} , Player B: {}".format(score_a,score_b),align="center",font=("Courier",20,"normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} , Player B: {}".format(score_a,score_b),align="center",font=("Courier",20,"normal"))

    #Collision

    if (ball.xcor() >340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40 ):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40 ):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)