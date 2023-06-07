import sys
inp = lambda: sys.stdin.readline()

ahdma = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
line = ''
while line != '#':
    line = sys.stdin.readline().strip()
    if line == '#':
        break
    print(len([c for c in line if c in ahdma]))
