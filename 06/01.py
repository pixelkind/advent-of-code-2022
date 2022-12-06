file = open('./input.txt', 'r')
string = file.read()

total_count = 0
chars = []
for char in string:
  if char in chars:
    index = chars.index(char) + 1
    chars = chars[index:]
  
  chars.append(char)
  total_count += 1
  if len(chars) == 4:
    break

print(total_count)