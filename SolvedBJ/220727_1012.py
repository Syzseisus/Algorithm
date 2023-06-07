import sys
from collections import deque


def BFS(row, col, count):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    q = deque()

    q.append((row, col))
    visited[row][col] = 1

    while q:
        i, j = q.popleft()

        for k in range(4):
            Y = i + dy[k]
            X = j + dx[k]

            if X > -1 and X < M and Y > -1 and Y < N:
                if farm[Y][X] and not visited[Y][X]:
                    q.append((Y, X))
                    count += 1
                    visited[Y][X] = 1

    answer.append(count)


T = int(sys.stdin.readline())

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    farm = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        farm[Y][X] = 1

    answer = []
    for row in range(N):
        for col in range(M):
            if farm[row][col] and not visited[row][col]:
                BFS(row, col, 1)

    print(len(answer))
