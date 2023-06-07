import sys
from collections import deque, defaultdict

inp = lambda: sys.stdin.readline()

N = int(inp())

tree = defaultdict(list)
for _ in range(N - 1):
    p, s = map(int, inp().strip().split())
    tree[p].append(s)

wb = [list(map(int, inp().strip().split())) for _ in range(N)]

cand = [] 
for color in [True, False]:
    start = 0
    temp = deque([0])
    while temp:
        t = len(temp)
        for i in range(t):
            node = temp.popleft()
            start += wb[node][color]
            temp.extend(tree[node])
        color = not color

    cand.append(start)

print(min(cand))