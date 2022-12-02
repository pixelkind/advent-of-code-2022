# A for Rock, B for Paper, C for Scissors
# X for Rock, Y for Paper, Z for Scissors
# score: 1 for Rock, 2 for Paper, and 3 for Scissors
# outcome of the round: 0 if you lost, 3 if the round was a draw, and 6 if you won

file = open('./input.txt', 'r')
string = file.read()
lines = string.split('\n')
# rounds = list(map(lambda s: s.split(' '), lines))

points = { 'X': 1, 'Y': 2, 'Z': 3 }
translate = { 'A': 'X', 'B': 'Y', 'C': 'Z' }

total_score = 0

for round in lines:
  values = round.split(' ')
  elf = translate[values[0]]
  me = values[1]
  total_score += points[me]
  # draw
  if elf == me:
    total_score += 3
  elif round == 'A Z' or round == 'B X' or round == 'C Y':
    total_score += 0
  else:
    total_score += 6

print(total_score)
