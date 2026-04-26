class A:
    def __init__(self):
        self.x = 10

class B(A):
    def __init__(self):
        super().__init__()
        self.y = 20

b = B()
print(b.x, b.y)







class Animal:
    def speak(self):
        return "sound"

class Cat(Animal):
    def speak(self):
        return super().speak() + " meow"

c = Cat()
print(c.speak())









class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

t = Teacher("Aruzhan", "Math")
print(t.name, t.subject)