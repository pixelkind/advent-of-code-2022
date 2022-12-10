file = open('./input.txt', 'r')
string = file.read()
lines = string.split('\n')

head_x = 0
head_y = 0
tail_x = 0
tail_y = 0

def move_tail_x():
  global tail_x
  if head_x > tail_x:
    tail_x += 1
  else:
    tail_x -= 1

def move_tail_y():
  global tail_y
  if head_y > tail_y:
    tail_y += 1
  else:
    tail_y -= 1

tail_positions = [(tail_x, tail_y)]
tail_visits = 1
def move_tail():
  global tail_x, tail_y, tail_visits

  visits = False
  dist_x = abs(head_x - tail_x)
  dist_y = abs(head_y - tail_y)
  if dist_x > 1 and dist_y == 1:
    visits = True
    move_tail_x()
    move_tail_y()
  elif dist_y > 1 and dist_x == 1:
    visits = True
    move_tail_x()
    move_tail_y()
  elif dist_x > 1 and dist_y == 0:
    visits = True
    move_tail_x()
  if dist_y > 1 and dist_x == 0:
    visits = True
    move_tail_y()

  if visits:
    tail_positions.append((tail_x, tail_y))
    tail_visits += 1

for line in lines:
  components = line.split(' ')
  moves = int(components[1])
  if components[0] == 'R':
    for _ in range(moves):
      head_x += 1
      move_tail()
  elif components[0] == 'L':
    for _ in range(moves):
      head_x -= 1
      move_tail()
  elif components[0] == 'U':
    for _ in range(moves):
      head_y -= 1
      move_tail()
  elif components[0] == 'D':
    for _ in range(moves):
      head_y += 1
      move_tail()

  # print(line, ': ', head_x, head_y, tail_x, tail_y, tail_visits)

print(tail_visits)
print(len(tail_positions))
print(len(set(tail_positions)))
print(head_x, head_y, tail_x, tail_y)