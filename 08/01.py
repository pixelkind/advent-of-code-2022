# how many trees are visible from outside the grid?

file = open('./input.txt', 'r')
string = file.read()
lines = string.split('\n')
lines = list(map(lambda x: list(x), lines))
lines = list(map(lambda x: list(map(lambda y: int(y), x)), lines))

def check_row(tree, x, y):
  visible_left = True
  for index in range(x - 1, -1, -1):
    if lines[y][index] >= tree:
      visible_left = False
      break
  
  visible_right = True
  for index in range(x + 1, len(lines[y])):
    if lines[y][index] >= tree:
      visible_right = False
      break

  return visible_left or visible_right

def check_column(tree, x, y):
  visible_top = True
  for index in range(y - 1, -1, -1):
    if lines[index][x] >= tree:
      visible_top = False
      break
  
  visible_bottom = True
  for index in range(y + 1, len(lines)):
    if lines[index][x] >= tree:
      visible_bottom = False
      break
  
  return visible_top or visible_bottom

count = 0
length = len(lines[0])
for x in range(0, length):
  for y in range(0, len(lines)):
    tree = lines[y][x]
    row = check_row(tree, x, y)
    column = check_column(tree, x, y)
    if row or column:
      count += 1

print(count)
