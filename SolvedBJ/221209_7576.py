from sys import stdin
from collections import deque

def main():
    M, N = map(int, stdin.readline().split())
    tomatoes = [list(stdin.readline().rstrip().split()) for _ in range(N)]

    ripe = deque()
    for r in range(N):
        for c in range(M):
            if tomatoes[r][c] == '1':
                ripe.append((r, c))

    if not ripe:
        print(-1)
        return 

    step = 0
    temp = deque()
    while True:
        r, c = ripe.popleft()
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr = r + dr
            nc = c + dc
            if not (0 <= nr < N and 0 <= nc < M):
                continue
            if tomatoes[nr][nc] == '0':
                tomatoes[nr][nc] = '1'
                temp.append((nr, nc))
        
        if not (ripe or temp):
            for r in range(N):
                for c in range(M):
                    if tomatoes[r][c] == '0':
                        print(-1)
                        return
            print(step)
            return

        if not ripe:
            step += 1
            ripe = temp
            temp = deque()

main()