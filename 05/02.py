file = open('./input.txt', 'r')
string = file.read()
components = string.split('\n\n')

stack_rows = components[0].split('\n')
procedures = components[1].split('\n')

stack_numbers = list(map(lambda x: int(x), stack_rows.pop().split('   ')))
number_of_stacks = len(stack_numbers)

stacks = []

for index in range(number_of_stacks):
  stack = []
  for row in stack_rows:
    crate = row[1 + 4 * index]
    if crate != ' ':
      stack.append(row[1 + 4 * index])
  stacks.append(stack)

for procedure in procedures:
  l = procedure.split(' ')
  amount = int(l[1])
  from_stack = int(l[3]) - 1
  to_stack = int(l[5]) - 1

  temp_list = []
  for _ in range(amount):
    temp_list.append(stacks[from_stack].pop(0))
  stacks[to_stack] = temp_list + stacks[to_stack]
    # stacks[to_stack].insert(0, crate)

result = ""
for stack in stacks:
  if len(stack) > 0:
    result += stack[0]

print(result)
