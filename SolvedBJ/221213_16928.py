from sys import stdin
from collections import deque as dq

N, M = map(int, stdin.readline().split())
warp = {}
for _ in range(N+M):
    x, y = map(int, stdin.readline().split())
    warp[x] = y

DP = [0 for _ in range(101)]
dice = range(1, 7)
visited = [False for _ in range(101)]

# 시작
q = dq([1])
visited[1] = True
while q:
    prev = q.popleft()

    if prev == 100:
        print(DP[-1])
        break

    for d in dice:
        curr = prev + d

        if 1 <= curr <= 100 and not visited[curr]:
            if curr in warp:
                curr = warp[curr]
            
            if not visited[curr]:
                q.append(curr)
                visited[curr] = True
                DP[curr] = DP[prev] + 1