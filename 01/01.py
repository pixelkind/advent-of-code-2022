import functools

file = open('./input.txt', 'r')
string = file.read()
elves = string.split("\n\n")

total_calories = list(map(lambda x: functools.reduce(lambda a, b: a + b, map(lambda y: int(y), x.split())), elves))
print(total_calories)
print(max(total_calories))
