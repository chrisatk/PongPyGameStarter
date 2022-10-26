# ICS2O Starter Code
# PONG Game
# Oct 2022
# Author: Chris Atkinson

import pygame, sys
from pygame.locals import QUIT
import random

# Initialize our display
pygame.init()
disp = pygame.display.set_mode((640,480))
# Give our game a title
pygame.display.set_caption('Pong')

# Set some variables
dispX,dispY = disp.get_size() # window size
paddleWidth = 5
paddleHeight = 75
# Starting position
player1X = 10
player2X = dispX-paddleWidth-10
player1Y = 10
player2Y = 10
speed = 10
ballX = round(dispX/2)
ballY = round(dispY/2)
ballRadius = 5
ballXDirection = random.randint(0,1)
ballYDirection = random.randint(-1,1)
// Prevent bouncing back and forth without a vertical change
while ballYDirection==0:
  ballYDirection = random.randint(-1,1)
ballXSpeed = random.randint(4,7)
ballYSpeed = random.randint(3,5)

while True:
  pygame.time.delay(100)
  # Exit the game cleanly
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()

  # Move the ball
  if ballXDirection == 1:
    ballX += ballXSpeed
    ballY += ballYDirection * ballYSpeed
  else:
    ballX -= ballXSpeed
    ballY += ballYDirection * ballYSpeed
    
  # Collect key presses
  keys = pygame.key.get_pressed()

  # Deal with player 2 paddle
  if keys[pygame.K_UP]:
    if player2Y < speed:
      player2Y = 0
    else: 
      player2Y -= speed    
      
  if keys[pygame.K_DOWN]:
    if player2Y > (dispY - (paddleHeight + speed)):
      player2Y = dispY-paddleHeight
    else: 
      player2Y += speed

  # Deal with player 1 paddle
  if keys[pygame.K_a]:
    if player1Y < speed:
      player1Y = 0
    else: 
      player1Y -= speed    
  if keys[pygame.K_z]:
    if player1Y > (dispY - (paddleHeight + speed)):
      player1Y = dispY-paddleHeight
    else: 
      player1Y += speed

  # erase previous position after a move
  disp.fill((0,0,0,0))

  # Draw the new position
  player1 = pygame.draw.rect(disp,[200,200,200],(player1X,player1Y,paddleWidth,paddleHeight))

  player2 = pygame.draw.rect(disp,[200,200,200],(player2X,player2Y,paddleWidth,paddleHeight))

  ball = pygame.draw.circle(disp,(200,200,200),(ballX,ballY),ballRadius)

  # Hanlde ball boundries and game over
  ### You need to finish the code in here to get Pong to work properly
  if player1.colliderect(ball):
    ballXDirection = -ballXDirection
  elif ballX < ballXSpeed or ballX > dispX-ballXSpeed:
    print("Game over")
    runGame = False
    
  # Refresh the display
  pygame.display.update()

  # Refresh the display
  pygame.display.update()
