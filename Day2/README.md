##Installation

If you have Python and pygame already installed on your computer, you should be good to go! Otherwise, the easiest way to get started is to go to http://helloworldbookblog.com/tools/ and download the installer for your operating system. This will include everything you need. We will be using Python version 2.X.

If there are installation issues, http://repl.it/ can be used for the first week. It cannot be used for the second week though, because graphics and pygame are required.

## Review of Python Classes

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



1. Give each student a favorite color property. Then write a method that will have the student tell us his favorite color.

2. Write a class method that will have each Student say his name and age and favorite color.

3. Create a few more students: `jane` and `betty`. Give them ages, names, and favorite colors.

4. Bonus: Give each student a best friend property (hint: use classes!). Write a method to return his/her best friend's name

## Constructors

In the last section, we were creating students without names and ages. We then gave names and ages to the students later. It doesn't make any sense to make Students with names and ages, so let's do the folowwing:

    def __init__(self, name, age):
        self.name = name
        self.age = age

Try to run your program again, and then use  the same console command as before:

    bobby = Student()

What happens?

You get an error. Since we have an constructor now, you can no longer create a Student without providing enough information to fill in the constructor arguments. Try this:

    bobby = Student("bobby", 10)

It should work.

The constructors in Python have the name `__init__`, and have an extra argument you do not need to provide when you instantiate an object - in this case: `self`.

## Lab - Deck of Cards

You will be implementing a deck of cards. Open up the file `DeckCards.py` in this directory inside IDLE.

1. Complete the card class. Each card has a suit (hearts, diamonds, spades, clubs) and a value (A, J, K, Q, 2-10)

2. Complete the deck class. Each deck will have 52 cards - 13 Hearts, 13 Spades, 13 Clubs, 13 Diamonds, each suit with cards A, J, K, Q, 2 to 10.

3. Complete the `dealCards` and `remainingCards` methods. See the code for details.

4. Now write a program that uses the Deck class to deal random cards.

5. Try to implement some simple card games using your Card and Deck classes.
