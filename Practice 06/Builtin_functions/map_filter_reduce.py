#MAPS

nums = [1, 2, 3]
res = list(map(lambda x: x * 2, nums))
print(res)

nums = [1, 2, 3]
print(list(map(lambda x: x + 1, nums)))

_____________________________
#FILTER

nums = [1, 2, 3, 4]
res = list(filter(lambda x: x % 2 == 0, nums))
print(res)

nums = [1, 2, 3, 4]
print(list(filter(lambda x: x>2, nums)))

_____________________________
#REDUCE

from functools import reduce
nums = [1, 2, 3, 4]
res = reduce(lambda x, y: x + y, nums)
print(res)  # 10

from functools import reduce
print(reduce(lambda x,y: x * y, [1,2,3]))
