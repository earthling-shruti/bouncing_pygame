#A simple game
import pygame
import random
import time

class Ball():

  def __init__(self):
    self.size = random.randrange(8, 20)
    self.x = random.randrange(20, size[0]-self.size)
    self.y = random.randrange(20, size[1]-self.size)
    self.color = [random.randrange(255) for i in range(3)]
    self.velocity_x = random.randrange(-10, 11, 1)/10.0
    self.velocity_y = random.randrange(-10, 11, 1)/10.0
    time.sleep(0.0004)

  def move(self):
    if self.velocity_x == 0 and self.velocity_y == 0:
      self.velocity_x = 1
    if self.x >= (size[0]-self.size) or self.x <= self.size:
      self.velocity_x = -self.velocity_x
    if self.y >= (size[1]-self.size) or self.y <= self.size:
      self.velocity_y = -self.velocity_y
    self.x += self.velocity_x
    self.y += self.velocity_y

  def draw(self, screen):
    pygame.draw.circle(screen, self.color, [int(self.x), int(self.y)], self.size)

pygame.init()
white = [255, 255, 255]
black = [0, 0, 0]
size = [600, 500]
clock = pygame.time.Clock()

screen = pygame.display.set_mode(size)
pygame.display.set_caption("bouncing balls")

balls = [Ball() for i in range(20)]

done = False
while not done :
  clock.tick(100)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True

  screen.fill(white)
  for ball in balls:
    ball.move()
    ball.draw(screen)
  pygame.display.flip()

pygame.quit()
