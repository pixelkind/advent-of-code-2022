file = open('./input.txt', 'r')
string = file.read()
lines = string.split('\n')

signal_strengths = [] # 20, 60, 100, 140, 180, 220
register_x = 1
cycle = 0
next_goal = 20
for line in lines:
  components = line.split(' ')
  command = components[0]
  add_to_cycle = 1
  value = 0
  if command == 'addx':
    add_to_cycle = 2
    value = int(components[1])
  
  new_cycle = cycle + add_to_cycle
  if new_cycle > next_goal:
    # print(next_goal, ': ', register_x, next_goal * register_x)
    signal_strengths.append(next_goal * register_x)
    next_goal += 40
  
  cycle += add_to_cycle

  if cycle == next_goal:
    # print(next_goal, ': ', register_x, next_goal * register_x)
    signal_strengths.append(next_goal * register_x)
    next_goal += 40

  register_x += value
  # print(cycle, ': ', register_x)
  
print(sum(signal_strengths))
