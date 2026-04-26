class A:
    x = 10

a1 = A()
a2 = A()

print(a1.x, a2.x)








class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

c1 = Counter()
c2 = Counter()

print(Counter.count)










class Student:
    school = "ABC School"

    def __init__(self, name):
        self.name = name

s1 = Student("Ali")
s2 = Student("Aruzhan")

print(s1.school, s2.school)
