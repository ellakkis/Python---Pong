from turtle import Turtle

class Ball(Turtle):

  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.color("red")
    self.penup()
    self.x_move = 10
    self.y_move = 10
    self.speed_timer = 0.1

  def move(self):
    new_x = self.xcor() + self.x_move
    new_y = self.ycor() + self.y_move
    self.goto(new_x, new_y)

  def bounce_y(self):
    self.y_move *= -1
    self.increase_speed()

  def bounce_x(self):
    self.x_move *= -1
    self.increase_speed()

  def reset_pos(self):
    self.goto(0, 0)
    
  def increase_speed(self):
    self.speed_timer *= 0.9