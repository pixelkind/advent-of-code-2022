file = open('./input.txt', 'r')
string = file.read()
lines = string.split('\n')
lines = list(map(lambda x: list(x), lines))
lines = list(map(lambda x: list(map(lambda y: int(y), x)), lines))

def check_row(tree, x, y):
  score_left = 0
  for index in range(x - 1, -1, -1):
    score_left += 1
    if lines[y][index] >= tree:
      break
  
  score_right = 0
  for index in range(x + 1, len(lines[y])):
    score_right += 1
    if lines[y][index] >= tree:
      break

  return score_left * score_right

def check_column(tree, x, y):
  score_top = 0
  for index in range(y - 1, -1, -1):
    score_top += 1
    if lines[index][x] >= tree:
      break
  
  score_bottom = 0
  for index in range(y + 1, len(lines)):
    score_bottom += 1
    if lines[index][x] >= tree:
      break
  
  return score_top * score_bottom

scenic_scores = []
length = len(lines[0])
for x in range(0, length):
  for y in range(0, len(lines)):
    tree = lines[y][x]
    row = check_row(tree, x, y)
    column = check_column(tree, x, y)
    result = row * column
    scenic_scores.append(result)

print(scenic_scores)
print(max(scenic_scores))
