import sys
from collections import deque

inp = lambda: sys.stdin.readline()

M, N = map(int, inp().split())


def BFS(row, col, cnt, case):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()

    q.append([row, col])
    visited[row][col] = 1

    while q:
        i, j = q.popleft()

        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            if nx > -1 and nx < N and ny > -1 and ny < M:
                if BF[nx][ny] == case and visited[nx][ny] == 0:
                    q.append([nx, ny])
                    cnt += 1
                    visited[nx][ny] = 1

    if case == "W":
        W.append(cnt**2)
    elif case == "B":
        B.append(cnt**2)


BF = [[i for i in inp().strip()] for _ in range(N)]
visited = [[0] * M for _ in range(N)]
W = []
B = []
for row in range(N):
    for col in range(M):
        if not visited[row][col]:
            BFS(row, col, 1, BF[row][col])

print(sum(W))
print(sum(B))
