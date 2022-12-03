# the first half of the characters represent items in the first compartment
# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52

file = open('./input.txt', 'r')
string = file.read()
lines = string.split('\n')

# find double items
items = []
for line in lines:
  l = int(len(line) / 2)
  c1 = line[:l]
  c2 = line[l:]

  for char in c1:
    if char in c2:
      items.append(char)
      break

# calculate priority
priority = 0
for item in items:
  if item.islower():
    priority += ord(item) - 96
  else:
    priority += ord(item) - 64 + 26

print(priority)