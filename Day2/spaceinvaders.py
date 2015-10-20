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

import pygame, sys, random
pygame.init()

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])

# List of missiles flying across the screen
player_missiles = []
alien_missiles = []
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

  def shoot(self):
    missile = Missile(self.xpos + 16, self.ypos - 1, -10)
    player_missiles.append(missile)

  def get_rect(self):
    return pygame.Rect(self.xpos, self.ypos, 32, 32)

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

  def move(self, x, y):
    self.xpos += x
    self.ypos += y

  def shoot(self):
    # Your code here!
    pass

  def get_rect(self):
    return pygame.Rect(self.xpos, self.ypos, 32, 32)

  def draw(self):
    # Your code here!
    pass


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

  def get_rect(self):
    return pygame.Rect(self.xpos, self.ypos, 2, 10)

  def isSpent(self):
    return self.spent

# Create all the objects and variables!
spaceship = Spaceship(200, 440)
aliens = []
# Make a grid of aliens
# Your code here!

running = True
ticks = 0
alien_formation_x = 0
alien_formation_x_speed = 10

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
    if len(player_missiles) == 0:
      spaceship.shoot()

  screen.fill(black)

  # Move, detect collisions, and draw the player's missiles
  for missile in player_missiles:
    missile.move()

    # Determine if the missile hit an alien. If so, the missile is spent
    # Your code here!

    if missile.isSpent():
      player_missiles.remove(missile)
    missile.draw()


  # Move, detect collisions, and draw the aliens' missiles
  for missile in alien_missiles:
    missile.move()
    # Detects collisions between the player and the alien missile
    # The player loses if they touch an alien missile
    # Your code here!

  # Move all the aliens
  # The more aliens there are, the slower they move
  if ticks % (len(aliens) + 1) == 0:
    # The alien formation moves left and right
    alien_formation_x += alien_formation_x_speed
    for alien in aliens:
      alien.move(alien_formation_x_speed, 0)
    # Until the formation reaches a limit, after which it reverses
    # direction and moves down 5 pixels
    if alien_formation_x >= 200 or alien_formation_x <= 0:
      alien_formation_x_speed = -1 * alien_formation_x_speed
      for alien in aliens:
        alien.move(0, 5)

  # Draw all the aliens and give them a chance to shoot!
  for alien in aliens:
    alien.draw()
    # Aliens shoot randomly
    # Your code here!

  # If there are no more aliens, the player wins
  # If any alien reaches the bottom of the screen, the player loses
  # Your code here!

  # Draw the spaceship
  spaceship.draw()
  pygame.display.update()
  ticks = ticks + 1

pygame.quit()
