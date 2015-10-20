#Installation

If you have Python and pygame already installed on your computer, you should be good to go! Otherwise, the easiest way to get started is to go to http://helloworldbookblog.com/tools/ and download the installer for your operating system. This will include everything you need. We will be using Python version 2.X.

If there are installation issues, http://repl.it/ can be used for the first week. It cannot be used for the second week though, because graphics and pygame are required.

# Review of Python Classes

A class can be thought of as a blueprint that you can use to create many copies of something.

Each "copy" of the class can have their own set of variables (called properties), however, each copy shares the same set of actions it can do (called methods).

Classes begin with the `class` keyword, followed by the class name. Classes can be "instantiated" by calling the class name:

    class Person:
      name = ""

    bob = Person()
    bob.name = "Bob"

### Example

The following is a class called Book

    class Book:
        title = ""
        author = ""

As a warm up, type the class into Python and do the following:

1. Add a constructor to set the `title` and the `author` at the same time

2. Add a method to print out both the `title` and the `author`.

3. Create two books by different authors. Get each of them to print out their title and author.

# Project - Space Invaders!

We're going to use classes to make an arcade classic: Space Invaders!

## Running the code

Open up `spaceinvaders.py` using IDLE. Hit F5 or go to Run, Run Module to run the program.

You should see your green spaceship. You can move this spaceship by pressing and holding the left and right keys. You can shoot by pressing space. So far, there's not a lot to shoot. This isn't much fun, is it?

Over the course of this class, we'll implement aliens that you can shoot, and who will also shoot back at you!

## Code walkthrough

At the top of the code, we have two functions (not part of any class) that are used for detecting whether rectangles intersect. This is library code borrowed from the book Invent with Python.

We then define a screen size, initialize pygame, and create the screen that we're going to be using to implement the game

    pygame.init()

    SCREEN_WIDTH = 640
    SCREEN_HEIGHT = 480

    screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])

This is followed by some arrays: `player_missiles` and `alien_missiles`. These arrays contain the missiles that the player and the aliens shoot at each other. At the moment, they're empty.

After that come our classes. The first class is our Spaceship. This class has three properties: an X position on the screen, a Y position, and a picture. In this case, we're going to load up `spaceship.png` from the directory that this file is in.

    class Spaceship:
      xpos = 0
      ypos = 0
      picture = pygame.image.load('spaceship.png')

We then have a constructor that requires defining the x and y positions of the spaceship

    def __init__(self, x, y):
      self.xpos = x
      self.ypos = y

We also have 5 methods:

1. `moveRight` - Moves the ship 5 pixels to the right
2. `moveLeft` - Moves the ship 5 pixels to the left
3. `shoot` - Creates a missile object with a position near the ship and adds it to the global player missile array
4. `get_rect` - Gets the bounding rectangle for the player. This is used to calculate if the player got hit
5. `draw` - Blits the player's picture at the right position on the screen

We also have classes for Aliens and Missiles. Notice that they are all very, very similar to one another. Hmm...

After the classes, we have an event loop that does the following things
1. Detects key presses from the player and makes the player's ship do things
2. Moves the player's misiles around and draws them
3. Moves the aliens' missiles around and draws them (TO DO!)
4. Moves the aliens around and draws them
5. Detects whether all the aliens are gone, or if one has reached the bottom (TO DO!)

## Finishing up the basic game

At the moment, we need to make this a game! We'll need to add aliens, give them the ability to shoot, and add win/lose conditions for the player.

### Making aliens

We'll need to make some aliens to make the game interesting. In order to do this, we'll need to put some aliens in the alien array.

    aliens = []
    # Make a grid of aliens
    # Your code here!

Make a 8 by 4 grid of aliens. Remember that the constructor for the Alien class requires an x and y position! (x = horizontal position, y = vertical)

Hint: Use for loops - one for the horizontal and one for the vertical direction

### Completing the Alien class

So, we've made a couple aliens, but if we run the program, we can't see them! Where are they?

This is because we don't have any code for the aliens' `draw` method. Let's complete the draw method!

Next up is the `shoot` method. It wouldn't be fun if the aliens couldn't shoot, right?

Finally, we'll need to tell the aliens when to shoot. Keep in mind that there are many of them, and the event loop is very fast. In this part of the code:

    for alien in aliens:
      alien.draw()
      # Aliens shoot randomly
      # Your code here!

You need to tell when the aliens when to shoot. (Hint: use random.randint !)

### Detecting collisions between Aliens and player missiles

Now we're getting somewhere - we can shoot the aliens and they can shoot us. However, something is wrong - the missiles fly right by and do nothing!

We'll need to figure out when missiles collide with aliens. In this part of the code:

    # Move, detect collisions, and draw the player's missiles
      for missile in player_missiles:
        missile.move()
        # Determine if the missile hit an alien. If so, the missile is spent
        # Your code here!

Figure out when the missile has hit any of the aliens.

Hint #1: Loop over the list of aliens and use `doRectsOverlap`. What are the `get_rect()` methods for?

Hint #2: When an alien is hit, remove it from the list of aliens and make the missile "spent"

### Winning and Losing conditions

In Space Invaders, the player wins when the player has shot all the aliens. The player loses when they either get shot by an alien, or if an alien reaches the bottom of the screen.

Let's implement these conditions. First, let's check to see if the player has gotten shot (the spaceship overlaps with an alien's missile) by adding a check to this section of code. The player should immediately lose (and the game is over) whenever the spaceship is hit.

    for missile in alien_missiles:
        missile.move()
        # Detects collisions between the player and the alien missile
        # The player loses if they touch an alien missile
        # Your code here!

Hint: Take a look at the example for when a player missile hits an alien

Hint: The game is over when `running` is set to `False`


Finally, we need to see if there are any aliens left, or if an alien reaches the bottom of the screen. The player wins if there are no more aliens, but loses if any of the aliens reach the bottom!

Hint: Loop through the aliens to see if any of them have a `ypos` greater than a certain amount...


## Projects!

We now have a complete, but extremely basic game of space invaders. The rest of this class is to make this game _awesome_.

### 1. Make the alien change pictures every frame

In space invaders, the aliens look different every single frame. There's another picture in here called `alien2.png`. Use it and change the appearance of all the aliens every single frame.

(Hint: Change the alien's picture every time its move method is called)

### 2. Keep score

It's much more fun when we can keep the player's score. Whenever the player shoots an alien, give the player 25 points. Then, make a point display to show the player. Here's some of the boilerplate code for adding text to the screen:

    myfont = pygame.font.SysFont("Arial", 15)
    score_label = myfont.render(str(score1), 1, pygame.color.THECOLORS['white'])
    screen.blit(score1_labe, (5, 10))

### 3. Give the player multiple lives

The player shouldn't automatically die whenever they get shot - they should have 3 lives. The player only loses when they lose all 3 of their lives. Make a display for letting the player know how many lives they have left next to the score display.

### 4. Make a flying saucer zip across the top of the screen

Remember how there was a saucer that sometimes appears at the top of the screen in space invaders? Let's implement that!

Make a new class called Saucer, use the `saucer.png` image provided in this repo, and every now and then, move a saucer from the right to the left across the very top of the screen.

Whenever the player shoots the saucer, give the player 100 points.

### Other ideas

- Give the aliens an explosion animation whenever they get shot
- Make a YOU WIN and a YOU LOSE screen in the pygame window
- The aliens' movement isn't too great - they stay in formation even after most of them are gone. Can you make smaller formations of aliens more challenging to shoot?
- Give the player some shields (they can take some hits) to hide behind
- Make different kinds of aliens - there's only 1 kind right now

## Further reading

Remember at the beginning of the class we noted how similar the player, alien, and missile classes were? Doesn't the code look very similar too? This is where `inheritence` comes into play. In Object Oriented Programming, inheritence is a way of saying that "this class is a kind of this other class". For example, an Orange is a Fruit, or a Dog is an Animal.

Recommended reading is here: https://docs.python.org/2/tutorial/classes.html .

Special challenge is to re-write the Player, Alien, and Missiles classes to all inherit from a common class, so we don't have to reimplement `draw` for any of them.
