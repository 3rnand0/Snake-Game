#MVP https://docs.replit.com/tutorials/build-snake-with-pygame

import pygame
from snake import * 

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