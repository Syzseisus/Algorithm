from sys import stdin

INF = float('inf')

N = int(stdin.readline())
graph = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j, edge in enumerate(stdin.readline().rstrip().split()):
        graph[i][j] = 1 if edge == '1' else INF

for via in range(N):
    for src in range(N):
        for dst in range(N):
            graph[src][dst] = min(graph[src][dst], graph[src][via] + graph[via][dst])

for i in range(N):
    for j in range(N):
        if graph[i][j] == INF:
            print("0", end=' ')
        else:
            print("1", end=' ')
    print()