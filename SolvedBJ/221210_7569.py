from sys import stdin
from collections import deque

def main():
    M, N, H = map(int, stdin.readline().split())
    tomatoes = [[list(stdin.readline().rstrip().split()) for _ in range(N)] for _ in range(H)]

    ripe = deque()
    for h in range(H):
        for r in range(N):
            for c in range(M):
                if tomatoes[h][r][c] == '1':
                    ripe.append((h, r, c))

    if not ripe:
        print(-1)
        return 

    step = 0
    temp = deque()
    while True:
        h, r, c = ripe.popleft()
        for dh, dr, dc in ((-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)):
            nh = h + dh
            nr = r + dr
            nc = c + dc
            if not (0 <= nh < H and 0 <= nr < N and 0 <= nc < M):
                continue
            if tomatoes[nh][nr][nc] == '0':
                tomatoes[nh][nr][nc] = '1'
                temp.append((nh, nr, nc))
        
        if not (ripe or temp):
            for h in range(H):
                for r in range(N):
                    for c in range(M):
                        if tomatoes[h][r][c] == '0':
                            print(-1)
                            return
            print(step)
            return

        if not ripe:
            step += 1
            ripe = temp
            temp = deque()

main()