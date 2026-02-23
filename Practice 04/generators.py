#Iterators

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

__________________________________

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

__________________________________

#Looping Through an Iterator

mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)

__________________________________

mystr = "banana"

for x in mystr:
  print(x)

__________________________________

#Create an Iterator

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

__________________________________

#Generators: yield keyword

def fun():
    yield 1            
    yield 2            
    yield 3

for val in fun(): 
    print(val)

__________________________________

#Creating Generator Functions

def fun(max):
    cnt = 1
    while cnt <= max:
        yield cnt
        cnt += 1

ctr = fun(5)
for n in ctr:
    print(n)

__________________________________

#Generator Expressions

sq = (x*x for x in range(1, 6))
for i in sq:
    print(i)