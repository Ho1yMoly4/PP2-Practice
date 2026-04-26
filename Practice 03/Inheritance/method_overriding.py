class Animal:
    def speak(self):
        return "sound"

class Dog(Animal):
    def speak(self):
        return "bark"

d = Dog()
print(d.speak())










class Shape:
    def area(self):
        return 0

class Square(Shape):
    def area(self):
        return 4 * 4

s = Square()
print(s.area())









class Bird:
    def fly(self):
        return "flying"

class Penguin(Bird):
    def fly(self):
        return "cannot fly"

p = Penguin()
print(p.fly())