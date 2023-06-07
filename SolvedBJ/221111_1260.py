from sys import stdin
from collections import deque as dq
from collections import defaultdict as ddict

graph = ddict(list)

N, M, start = map(int, stdin.readline().split())
for _ in range(M):
    src, tgt = map(int, stdin.readline().split())
    graph[src].append(tgt)
    graph[tgt].append(src)

for i in graph:
    graph[i].sort()

dfs_visited = set([start])
def dfs(curr):
    dfs_visited.add(curr)
    print(curr, end=' ')
    for nbr in graph[curr]:
        if nbr not in dfs_visited:
            dfs(nbr)
dfs(start)
print()

bfs_visited = set([start])
bfs = dq([start])
while bfs:
    curr = bfs.popleft()
    print(curr, end=' ')
    for nbr in graph[curr]:
        if nbr not in bfs_visited:
            bfs.append(nbr)
            bfs_visited.add(nbr)