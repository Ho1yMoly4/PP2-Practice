class Animal:
    def speak(self):
        return "sound"

class Dog(Animal):
    pass

d = Dog()
print(d.speak())









class Vehicle:
    def move(self):
        return "moving"

class Car(Vehicle):
    def wheels(self):
        return 4

c = Car()
print(c.move(), c.wheels())






class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def get_name(self):
        return self.name

s = Student("Ali")
print(s.get_name())