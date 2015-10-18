#Credit the Invent With Python book (http://inventwithpython.com)
#for doRectsOverlap and isPointInsideRect functions

#used to detect collisions in our game
def doRectsOverlap(rect1, rect2):
    for a, b in [(rect1, rect2), (rect2, rect1)]:
        # Check if a's corners are inside b
        if ((isPointInsideRect(a.left, a.top, b)) or
            (isPointInsideRect(a.left, a.bottom, b)) or
            (isPointInsideRect(a.right, a.top, b)) or
            (isPointInsideRect(a.right, a.bottom, b))):
            return True

    return False

#used the by the doRectsOverlap function (won't be called directly from game code)
def isPointInsideRect(x, y, rect):
    if (x > rect.left) and (x < rect.right) and (y > rect.top) and (y < rect.bottom):
        return True
    else:
        return False

import pygame, sys
pygame.init()

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])

class Spaceship:
  xpos = 0
  ypos = 0

  def __init__(self, x, y):
    self.xpos = x
    self.ypos = y

class Alien:
  xpos = 0
  ypos = 0
  xspeed = 2
  picture = pygame.image.load('alien1.png')

  def __init__(self, x, y):
    self.xpos = x
    self.ypos = y


class Missile:
  xpos = 0
  ypos = 0
  xspeed = 2
  yspeed = 2

  def __init__(self, x, y):
    self.xpos = x
    self.ypos = y

