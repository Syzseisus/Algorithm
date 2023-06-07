from sys import stdin, setrecursionlimit
from collections import defaultdict as ddict

setrecursionlimit(100000)

N, M = map(int, stdin.readline().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)


visited = [False] * (N + 1)
def dfs(node):
    for ngbr in graph[node]:
        if not visited[ngbr]:
            visited[ngbr] = True
            dfs(ngbr)


answer = 0
for node in range(1, N + 1):
    if not visited[node]:
        visited[node] = True
        dfs(node)
        answer += 1
print(answer)