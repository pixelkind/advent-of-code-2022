file = open('./input.txt', 'r')
string = file.read()
lines = string.split('\n')

position = []
for _ in range(10):
  position.append((0, 0))

def move_tail_x(head_x, tail_x):
  if head_x > tail_x:
    tail_x += 1
  else:
    tail_x -= 1
  return tail_x

def move_tail_y(head_y, tail_y):
  if head_y > tail_y:
    tail_y += 1
  else:
    tail_y -= 1
  return tail_y

tail_positions = [(0, 0)]
def move_tail(index):
  global position

  head_x = position[index-1][0]
  head_y = position[index-1][1]
  tail_x = position[index][0]
  tail_y = position[index][1]
  dist_x = abs(head_x - tail_x)
  dist_y = abs(head_y - tail_y)
  if dist_x > 1 and dist_y >= 1:
    tail_x = move_tail_x(head_x, tail_x)
    tail_y = move_tail_y(head_y, tail_y)
  elif dist_y > 1 and dist_x >= 1:
    tail_x = move_tail_x(head_x, tail_x)
    tail_y = move_tail_y(head_y, tail_y)
  elif dist_x > 1 and dist_y == 0:
    tail_x = move_tail_x(head_x, tail_x)
  elif dist_y > 1 and dist_x == 0:
    tail_y = move_tail_y(head_y, tail_y)

  if index == len(position)-1:
    tail_positions.append((tail_x, tail_y))
  
  position[index] = (tail_x, tail_y)
  if index < len(position) - 1:
    move_tail(index+1)

for line in lines:
  components = line.split(' ')
  moves = int(components[1])
  print(moves)
  head_x = position[0][0]
  head_y = position[0][1]
  if components[0] == 'R':
    for _ in range(moves):
      head_x += 1
      position[0] = (head_x, head_y)
      move_tail(1)
  elif components[0] == 'L':
    for _ in range(moves):
      head_x -= 1
      position[0] = (head_x, head_y)
      move_tail(1)
  elif components[0] == 'U':
    for _ in range(moves):
      head_y -= 1
      position[0] = (head_x, head_y)
      move_tail(1)
  elif components[0] == 'D':
    for _ in range(moves):
      head_y += 1
      position[0] = (head_x, head_y)
      move_tail(1)

  print(position)

print(len(tail_positions))
print(len(set(tail_positions)))