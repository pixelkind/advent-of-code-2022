from dataclasses import dataclass

@dataclass
class Directory:
  name: str
  directories: list
  files: list
  parent: any = None

  def size(self) -> int:
    size = 0
    for dir in self.directories:
      size += dir.size()
    for file in self.files:
      size += file.size
    return size

@dataclass
class File:
  name: str
  size: int

file = open('./input.txt', 'r')
string = file.read()
lines = string.split('\n')

root = Directory("root", [], [])

current_directory = root
for line in lines:
  if line.startswith('$'):
    # a command
    if line.startswith('$ cd '):
      print('change dir')
      dir_command = line.split('$ cd ').pop()
      print(dir_command)
      if dir_command == '..':
        print('one folder up')
        current_directory = current_directory.parent
      elif dir_command == '/':
        print('back to the root')
        current_directory = root
      else:
        print('foldername', line)
        current_directory = next(filter(lambda x: x.name == dir_command, current_directory.directories), None)
    elif line.startswith('$ ls'):
      print('list')
  elif line.startswith('dir'):
    # a directory
    components = line.split(' ')
    dir = Directory(components[1], [], [], current_directory)
    current_directory.directories.append(dir)
  else:
    # a file
    components = line.split(' ')
    file = File(components[1], int(components[0]))
    current_directory.files.append(file)

print(root.size())

# 70000000
# 30000000

size_needed = abs(70000000 - 30000000 - root.size())
print(size_needed)

directory_sizes = []

def check_size(dir):
  global directory_sizes
  size = dir.size()
  if size >= size_needed:
    directory_sizes.append(size)

def check_dir(directory):
  for dir in directory.directories:
    check_size(dir)
    check_dir(dir)

check_size(root)
check_dir(root)

print(min(directory_sizes))