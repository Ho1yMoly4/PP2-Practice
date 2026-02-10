def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


_______________________

def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Adil") # "Adil" is an argument


_______________________

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")


_______________________

def my_function(name = "friend"):
  print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")


_______________________
#Keyword arguments:

def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy")


__________________________
#Positional arguments:

def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("dog", "Buddy")
