file = open('./input.txt', 'r')
string = file.read()
lines = string.split('\n')

# find triple items
items = []
for i in range(0, len(lines), 3):
  e1 = lines[i]
  e2 = lines[i+1]
  e3 = lines[i+2]

  for char in e1:
    if char in e2 and char in e3:
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