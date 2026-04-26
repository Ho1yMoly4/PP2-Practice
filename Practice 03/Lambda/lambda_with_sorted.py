students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)




words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)



nums = [5, 2, 9, 1]
nums.sort(key=lambda x: x)
print(nums)




pairs = [(1, 3), (2, 1), (4, 2)]
pairs.sort(key=lambda x: x[1])
print(pairs)