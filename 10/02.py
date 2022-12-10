file = open('./input.txt', 'r')
string = file.read()
lines = string.split('\n')

register_x = 1
cycle = 0

screen = ''
for line in lines:
  components = line.split(' ')
  command = components[0]
  add_to_cycle = 1
  value = 0

  if command == 'addx':
    add_to_cycle = 2
    value = int(components[1])
  
  new_cycle = cycle + add_to_cycle

  for _ in range(add_to_cycle):
    cycle += 1
    cycle_pos = cycle % 40 - 1
    if abs(cycle_pos - register_x) <= 1:
      screen += '#'
    else:
      screen += ' '
    
    if cycle % 40 == 0:
      screen += '\n'

  register_x += value

print(screen)
