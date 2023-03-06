from turtle import Turtle

class Scoreboard(Turtle):

  def __init__(self, position):
      super().__init__()
      self.score = 0
      self.update_scoreboard(position)
    
  def update_scoreboard(self, position):
      self.clear()
      self.penup()
      self.hideturtle()
      self.color("white")
      self.goto(position)
      self.write(f"{self.score}", font=('Courier', 40, 'normal'))
    
    


  def increase_score(self, position):
      self.score += 1
      self.update_scoreboard(position)


  
    

  