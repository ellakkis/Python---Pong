from turtle import Turtle


class Paddle(Turtle):

  def __init__(self, position):
    super().__init__()
    self.shape("square")
    self.color("white")
    self.shapesize(stretch_len=5)
    self.penup()
    self.seth(90)
    self.goto(position)


  def move_up(self):
    self.forward(30)

  def move_down(self):
    self.backward(30)
