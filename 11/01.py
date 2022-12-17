# Count the total number of times each monkey inspects items over 20 rounds

from dataclasses import dataclass

@dataclass
class Monkey:
  number: int
  items: list
  operation: str
  division_test: int
  true_monkey: int
  false_monkey: int
  inspections: int = 0

  def inspect(self, item) -> int:
    self.inspections += 1
    operation = self.operation.split(' ')
    operator = operation[0]
    value_string = operation[1]
    if value_string == 'old':
      value = item
    else:
      value = int(value_string)
    
    if operator == '*':
      return item * value
    elif operator == '+':
      return item + value
    return item

file = open('./input.txt', 'r')
string = file.read()
monkey_strings = string.split('\n\n')

monkeys = []
for monkey_string in monkey_strings:
  lines = monkey_string.split('\n')
  number = int(lines[0].split(' ')[1][:-1])
  items = lines[1].split('  Starting items: ').pop(-1).split(', ')
  items = list(map(lambda x: int(x), items))
  operation = lines[2].split('  Operation: new = old ').pop(-1)
  division = int(lines[3].split('  Test: divisible by ').pop(-1))
  true_monkey = int(lines[4].split('    If true: throw to monkey ').pop(-1))
  false_monkey = int(lines[5].split('    If false: throw to monkey ').pop(-1))

  monkey = Monkey(number, items, operation, division, true_monkey, false_monkey)
  monkeys.append(monkey)

# before it tests your worry level, your worry level to be divided by three and rounded down to the nearest integer

for i in range(20):
  for monkey in monkeys:
    for index, item in enumerate(monkey.items):
      item = int(monkey.inspect(item) / 3)
      monkey.items[index] = item
      if item % monkey.division_test == 0:
        monkeys[monkey.true_monkey].items.append(item)
      else:
        monkeys[monkey.false_monkey].items.append(item)
    monkey.items = []

inspections = []
for monkey in monkeys:
  inspections.append(monkey.inspections)

inspections.sort(reverse=True)
result = inspections[0] * inspections[1]
print(result)