from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())
maze = [[int(i) for i in stdin.readline().rstrip()] for _ in range(N)]

q = deque([(0, 0)])
while q:
    r, c = q.popleft()

    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nr = r + dr
        nc = c + dc
        if ((0 <= nr < N) and (0 <= nc < M) and maze[nr][nc]):
            if maze[nr][nc] == 1:
                maze[nr][nc] = maze[r][c] + 1
                q.append((nr, nc))
            elif maze[nr][nc] > maze[r][c] + 1:
                maze[nr][nc] = maze[r][c] + 1
                q.append((nr, nc))

print(maze[-1][-1])