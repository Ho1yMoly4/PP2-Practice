f = open("demofile.txt")

f = open("demofile.txt", r)

f = open("demofile.txt", a)

f = open("demofile.txt", w)

f = open("demofile.txt", x)

_______________________________________

f = open("demofile.txt")
print(f.read())

f = open("D:\\myfiles\welcome.txt")
print(f.read())

with open("demofile.txt") as f:
  print(f.read())

f = open("demofile.txt")
print(f.read())
f.close()

with open("demofile.txt") as f:
  print(f.read(5))

with open("demofile.txt") as f:
  print(f.readline())

with open("demofile.txt") as f:
  print(f.readlines())

  