from sys import stdin
from collections import defaultdict

N = int(stdin.readline())
graph = defaultdict(list)
for _ in range(int(stdin.readline())):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

network = [0 for _ in range(N + 1)]
def dfs(x):
    network[x] = 1
    for node in graph[x]:
        if network[node] == 0:
            dfs(node)

dfs(1)
print(sum(network) - 1)