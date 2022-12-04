# In how many assignment pairs do the ranges overlap?

file = open('./input.txt', 'r')
string = file.read()
lines = string.split('\n')

def range_from_string(string):
  numbers = string.split('-')
  return range(int(numbers[0]), int(numbers[1]) + 1)

count = 0
for line in lines:
  pair = line.split(',')
  r1 = range_from_string(pair[0])
  r2 = range_from_string(pair[1])
  if not set(r1).isdisjoint(r2) or not set(r2).isdisjoint(r1):
    count += 1

print(count)