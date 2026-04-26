class A:
    def a(self):
        return "A"

class B:
    def b(self):
        return "B"

class C(A, B):
    pass

c = C()
print(c.a(), c.b())












class X:
    def show(self):
        return "X"

class Y:
    def show(self):
        return "Y"

class Z(X, Y):
    pass

z = Z()
print(z.show())















class Father:
    def skill1(self):
        return "driving"

class Mother:
    def skill2(self):
        return "cooking"

class Child(Father, Mother):
    pass

c = Child()
print(c.skill1(), c.skill2())