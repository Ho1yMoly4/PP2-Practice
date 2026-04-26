numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)




nums = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x: x % 2 == 0, nums))
print(even)




words = ["apple", "hi", "banana", "ok"]
long_words = list(filter(lambda x: len(x) > 3, words))
print(long_words)




nums = [-5, 3, -1, 7, 0]
positive = list(filter(lambda x: x > 0, nums))
print(positive)