#MVP https://docs.replit.com/tutorials/build-snake-with-pygame

import pygame
from snake import * 
from food import *

#Creating the window for Snake  game
pygame.init()
bounds = (300,300)
window = pygame.display.set_mode(bounds)
pygame.display.set_caption("Snake")
block_size = 20
snake = Snake(block_size, bounds)

run = True
while run:
  pygame.time.delay(100)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  window.fill((0,0,0))
  snake.draw(pygame, window)
  pygame.display.flip()
  
  run = True
while run:
  pygame.time.delay(100)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT]:
    snake.steer(Direction.LEFT)
  elif keys[pygame.K_RIGHT]:
    snake.steer(Direction.RIGHT)
  elif keys[pygame.K_UP]:
    snake.steer(Direction.UP)
  elif keys[pygame.K_DOWN]:
    snake.steer(Direction.DOWN)

  snake.move()
  window.fill((0,0,0))
  snake.draw(pygame, window)
  pygame.display.update()
