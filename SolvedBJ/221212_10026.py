from sys import stdin, setrecursionlimit
setrecursionlimit(10000)

N = int(stdin.readline())
colormap = [[i for i in stdin.readline().rstrip()] for _ in range(N)]

def search(r, c):
    visited[r][c] = True
    RGB = colormap[r][c]
    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nr = r + dr
        nc = c + dc
        if (((0 <= nr < N) and (0 <= nc < N)) and
            not visited[nr][nc] and
            colormap[nr][nc] == RGB):
            search(nr, nc)

# Normal
normal = 0
visited = [[False for _ in range(N)] for _ in range(N)]
for r in range(N):
    for c in range(N):
        if not visited[r][c]:
            search(r, c)
            normal += 1

# Change Colormap
for r in range(N):
    for c in range(N):
        if colormap[r][c] == 'R':
            colormap[r][c] = 'G'

# Weak
weak = 0
visited = [[False for _ in range(N)] for _ in range(N)]
for r in range(N):
    for c in range(N):
        if not visited[r][c]:
            search(r, c)
            weak += 1

print(normal, weak)
