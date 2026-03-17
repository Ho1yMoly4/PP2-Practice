#ENUMERATE

a = ["a", "b", "c"]
for i, v in enumerate(a):
    print(i, v)


print(list(enumerate([10,20,30])))

_____________________________
#ZIP

a = [1, 2]
b = ["a", "b"]
print(list(zip(a, b)))

a = [1,2,3]
b = [4,5,6]
for x, y in zip(a,b):
    print(x+y)