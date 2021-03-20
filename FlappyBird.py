import turtle
import time
import random
import math



screen = turtle.Screen()
screen.tracer(0)

screen.addshape("flappyBird.png")
screen.addshape("pipes.png")
screen.addshape("background.jpg")
screen.bgpic("background.jpg")

pipes = []

pauseGame = False
dead = False

class birb(turtle.Turtle):
  def __init__(self,xCor , yCor):
    turtle.Turtle.__init__(self)
    self.penup()
    self.speed(0)
    self.hideturtle()
    self.shape("birb.png")
    self.left(90)
    self.x = -100
    self.y = 0
    self.yspd = 3
    self.goto(self.x,self.y)
    self.showturtle()
    
  
  def flap(x):
    birb.yspd =7
    
  def flapAI(EYRE):
    birb.yspd =7
 
  def animate(self):
    if(self.yspd > 2):
      self.shape("flappyBird.png")
      self.setheading(105)
    elif(self.yspd < -2):
      self.shape("flappyBird.png")
      self.setheading(75)
    else:
      self.shape("flappyBird.png")
      self.setheading(90)
      
def getTrainingData():
  print("vertical distance to ground: " + str(birb.y + 200))
  print("horizontal distance to next pipe: " + str(pipe.x - birb.x))
  print("angle to next target: " + str(math.degrees(math.tan((pipe.y-birb.y)/(pipe.x-birb.x)))))
  

 
class pipe(turtle.Turtle):
  def __init__(self):
    turtle.Turtle.__init__(self)
    self.penup()
    self.speed(0)
    self.hideturtle()
    self.shape("pipes.png")
    self.left(90)
    self.x = 500
    self.y = 0
    self.xspd = 6
    self.goto(self.x,self.y)
    self.showturtle()
    pipes.append(self)
  

def moveAllPipes():
  for x in range(len(pipes)):
    pipes[x].x -= pipes[x].xspd
    if(pipes[x].x < -300):
      pipes[x].x = 250
      pipes[x].y = random.randint(-140,150)
    pipes[x].goto(pipes[x].x,pipes[x].y) 
 
 

def checkForDeath():
  global dead
  if(birb.y <= -200):
    pause()
    dead = True
  for x in range(len(pipes)):
    if(birb.x > pipes[x].x-50 and birb.x < pipes[x].x+50 and (birb.y > pipes[x].y+40 or birb.y < pipes[x].y-60)):
      pause()
      dead = True      
 
def physics():
  birb.yspd -= 0.3
  birb.yspd *= 0.95                  
  birb.y += birb.yspd
  
  if(birb.y > 200):
    birb.y = 200
  if(birb.y < -200):
    birb.y = -200
  
  birb.goto(birb.x, birb.y)
  
def pause():
  global pauseGame
  if(pauseGame == False):
    pauseGame = True
  else:
    pauseGame = False
  
  
def dumbAI():
  if(birb.y < pipe.y-50):
    birb.flapAI()

birb = birb(0,0) 
pipe = pipe()

screen.onkey(birb.flap, "space")  
screen.onkey(pause, "shift")
screen.onkey(getTrainingData,"z")
screen.listen()



while (not dead):
  while (pauseGame == False):
    physics()
    dumbAI()
    birb.animate()
    moveAllPipes() 
    screen.update()
    checkForDeath()
    
























