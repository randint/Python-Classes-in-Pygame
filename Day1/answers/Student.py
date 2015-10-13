
class Student:
    age = 0
    name = ""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_name(self):
        print "my name is " + self.name

    def say_age(self):
        print "my age is " + str(self.age)


bobby = Student("bobby", 10)

bobby.say_name()
bobby.say_age()
