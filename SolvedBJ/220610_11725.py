import sys
from collections import deque

N = int(sys.stdin.readline())

tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    l, r = map(int, sys.stdin.readline().split())
    tree[l].append(r)
    tree[r].append(l)


parent = [[] for _ in range(N + 1)]
q = deque()
q.append(1)
visit = [False for _ in range(N + 1)]
while q:
    v = q.popleft()
    for num in tree[v]:
        if not visit[num]:
            q.append(num)
            parent[num].append(v)
            visit[num] = True


for nodes in parent[2:]:
    for v in nodes:
        print(v)
