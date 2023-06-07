import sys
from collections import defaultdict

inp = lambda: sys.stdin.readline()

N = int(inp())
M = int(inp())
choices = list(map(int, inp().strip().split()))
moves = inp().strip()

able = True
pathes = [{}]
curr = defaultdict(int)

for choice, move in zip(choices, moves):
    curr[choice] += 1 if move == "+" else -1
    if curr[choice] == 0:
        del curr[choice]
    
    for path in pathes:
        if curr.items() == path.items():
            able = False
            break
    else:
        pathes.append(curr.copy())

if curr == {}:
    able = False

print(1 if able else 0)