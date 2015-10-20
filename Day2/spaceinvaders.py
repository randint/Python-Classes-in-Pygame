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

# List of missiles flying across the screen
missiles = []
black = [0, 0, 0]
white = [255, 255, 255]

class Spaceship:
  xpos = 0
  ypos = 0
  picture = pygame.image.load('spaceship.png')

  def __init__(self, x, y):
    self.xpos = x
    self.ypos = y

  def moveRight(self):
    self.xpos += 5

  def moveLeft(self):
    self.xpos -= 5

  def fire(self):
    missile = Missile(self.xpos, self.ypos - 32, -10)
    missiles.append(missile)

  def draw(self):
    screen.blit(self.picture, (self.xpos, self.ypos))

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
  speed = 0
  spent = False

  def __init__(self, x, y, speed):
    self.xpos = x
    self.ypos = y
    self.speed = speed

  def draw(self):
    pygame.draw.rect(screen, white, [self.xpos, self.ypos, 2, 10], 2)

  def move(self):
    self.ypos += self.speed
    if self.ypos < 0 or self.ypos > SCREEN_HEIGHT:
      self.spent = True

  def isSpent(self):
    return self.spent

# Create all the objects and variables!
spaceship = Spaceship(200, 440)
aliens = []
running = True

# Main event loop. Here we:
# 1. Handle keyboard input for the player and move the player around
# 2. Move the missiles around
# 3. Move the aliens around
# 4. Detect collisions and handle them
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  keys = pygame.key.get_pressed()
  if keys[pygame.K_RIGHT]:
      spaceship.moveRight()
  if keys[pygame.K_LEFT]:
      spaceship.moveLeft()
  if keys[pygame.K_SPACE]:
      spaceship.fire()

  screen.fill(black)

  # Move and draw the missiles
  for missile in missiles:
    missile.move()
    if missile.isSpent():
      missiles.remove(missile)
    missile.draw()

  # Move all the aliens

  # Draw the spaceship
  spaceship.draw()
  pygame.display.update()

pygame.quit()
