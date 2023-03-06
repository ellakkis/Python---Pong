from turtle import Screen, Turtle
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
import time

TOP_WALL = 280
BOTTOM_WALL = -280
RIGHT_WALL = 380
LEFT_WALL = -380
RIGHT_PADDLE_COR = 580
LEFT_PADDLE_COR = -580
R_SCOREBOARD_POS = (-100, 220)
L_SCOREBOARD_POS = (100, 220)

# create the screen
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

# create the paddles
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

# create the scoreboards
r_scoreboard = Scoreboard(R_SCOREBOARD_POS)
l_scoreboard = Scoreboard(L_SCOREBOARD_POS)

# create the center dashed line (the net)
net = Turtle()
net.shape("square")
net.seth(90)
net.penup()
net.goto(0, -300)
net.pensize(10)
net.hideturtle()
net.color("white")
for y in range(-300, 300, 25):
  net.pendown()
  net.forward(20)
  net.penup()
  net.goto(0, y*2)

screen.onkey(right_paddle.move_up,"Up")
screen.onkey(right_paddle.move_down,"Down")

screen.onkey(left_paddle.move_up,"w")
screen.onkey(left_paddle.move_down,"d")

# create the ball
ball = Ball()
game_is_on = True

while game_is_on:
  time.sleep(ball.speed_timer)
  screen.update()
  ball.move()

  
# detect collision with top and bottom walls
  if ball.ycor() > TOP_WALL or ball.ycor() < BOTTOM_WALL:
    ball.bounce_y()
    
# detect collision with paddles
  if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
    ball.bounce_x()

  # detect if its a goal
  if ball.xcor() > RIGHT_WALL:
    r_scoreboard.increase_score(R_SCOREBOARD_POS)
    ball.reset_pos()
    ball.bounce_x()
  if ball.xcor() < LEFT_WALL:
    l_scoreboard.increase_score(L_SCOREBOARD_POS)
    ball.reset_pos()
    ball.bounce_x()

