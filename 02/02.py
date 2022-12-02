# A for Rock, B for Paper, C for Scissors
# X lose, Y draw, Z win
# score: 1 for Rock, 2 for Paper, and 3 for Scissors
# outcome of the round: 0 if you lost, 3 if the round was a draw, and 6 if you won

file = open('./input.txt', 'r')
string = file.read()
lines = string.split('\n')
rounds = list(map(lambda s: s.split(' '), lines))

shapepoints = { 'A': 1, 'B': 2, 'C': 3 }
endpoints = { 'X': 0, 'Y': 3, 'Z': 6 }
results = {
  'X': {
    'A': 'C',
    'B': 'A',
    'C': 'B'
  },
  'Y': {
    'A': 'A',
    'B': 'B',
    'C': 'C'
  },
  'Z': {
    'A': 'B',
    'B': 'C',
    'C': 'A'
  }
}

total_score = 0

for round in rounds:
  elf = round[0]
  result = round[1]
  total_score += endpoints[result]
  total_score += shapepoints[results[result][elf]]

print(total_score)
