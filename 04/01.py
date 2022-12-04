# In how many assignment pairs does one range fully contain the other?

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
  if set(r1).issubset(r2) or set(r2).issubset(r1):
    count += 1

print(count)