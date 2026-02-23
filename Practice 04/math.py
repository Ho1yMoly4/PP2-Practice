#Built-in Math Functions (min, max, abs, round, pow)

x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

__________________________________

x = abs(-7.25)

print(x)

__________________________________

x = pow(4, 3)

print(x)

__________________________________

#math Module Functions (sqrt, ceil, floor, sin, cos, pi, e)

import math

x = math.sqrt(64)

print(x)

__________________________________

import math

x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # returns 2
print(y) # returns 1

__________________________________

import math

x = math.pi

print(x)

__________________________________

import random

r = random.random()
print(r)

__________________________________

import random

a = random.randint(1, 10)
b = random.randint(1, 10)
print(a, b)
print(a + b) #Sum for example

__________________________________

import random

items = ["apple", "banana", "cherry"]
picked = random.choice(items)

print(picked)

__________________________________

import random

nums = [1, 2, 3, 4, 5]
random.shuffle(nums)
print(nums)

