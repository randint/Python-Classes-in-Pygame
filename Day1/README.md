##Installation

If you have Python and pygame already installed on your computer, you should be good to go! Otherwise, the easiest way to get started is to go to http://helloworldbookblog.com/tools/ and download the installer for your operating system. This will include everything you need. We will be using Python version 2.X.

If there are installation issues, http://repl.it/ can be used for the first week. It cannot be used for the second week though, because graphics and pygame are required.

## Review of Basic Python

### Functions and Arguments

Open Python IDLE, which should open a console window. Open a new Python window (File -> New Window).

Write a function called `greet_name` that will print the name that we input to the screen. After writing the function, save the python file (name it something that ends with `.py`), then hit `F5` to run the code in the console window.

(Hint: it starts with `def print_name`)

Test it out in the console after the program runs:

    >>> print_name("Yun")
    Hello, Yun

Now, let's make a new function that takes both a name and an age

    >>> greet_name_age("Yun", 28)
    Hello, Yun. You are 28 years old.

For an implementation of `print_name` and `greet_name_age`, check in the answers directory.

In all these cases, the values between the parenthesis are called "arguments". Functions can have many arguments as you need.

### Return Values

You can return values from functions

    def multiply(a,b):
        return a * b

Functions do work and "hide" details from other code. The technical term is "abstraction".

## Classes

A class can be thought of as a blueprint that you can use to create many copies of something.

Each "copy" of the class can have their own set of variables (called properties), however, each copy shares the same set of actions it can do (called methods)

### Example

Open a new file python file and type in:

    class Student:
        age = 0
        name = ""

Run it. What happens?

Nothing happens. This is because you have only created the definition of the class. We'll need to instantiate an object. In other words, we'll need to create a student out of the blueprint for a student.

    bobby = Student()

`bobby` is now created, but with no name and no age. Let's give him a name and an age

    bobby.name = "Bobby"
    bobby.age = 10

Run the program again. What happens?

Nothing happens again. But why is this?

Bobby is now created, but we haven't told him to do anything yet. Let's give him some actions. In your student class, type the following in:

    def say_name(self):
        print "my name is " + self.name

    def say_age(self):
        print "my age is " + str(self.age)

Run the file again. In the console, create bobby again and do this:

    bobby = Student()
    bobby.age = 10
    bobby.name = "Bobby"

    bobby.say_name()
    bobby.say_age()

What happens?

### Exercise

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
