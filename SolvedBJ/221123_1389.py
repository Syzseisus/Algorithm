'''
KB[a][b] = min(KB[a][b], KB[a][i] + KB[i][b])
'''

from sys import stdin

N, M = map(int, stdin.readline().split())
KB = [[float('inf') for _ in range(N)] for _ in range(N)]
for _ in range(M):
    A, B = map(int, stdin.readline().split())
    KB[A-1][B-1] = 1
    KB[B-1][A-1] = 1

for i in range(N):
    for a in range(N):
        for b in range(N):
            KB[a][b] = min(KB[a][b], KB[a][i] + KB[i][b])

answer = float('inf')
ind = float("inf")
for i, row in enumerate(KB):
    if sum(row) < answer:
        answer = sum(row)
        ind = i
print(ind + 1)