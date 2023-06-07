import sys

inp = lambda: sys.stdin.readline()

N, M = map(int, inp().split())
array = list(list(map(int, inp().split())) for _ in range(N))
dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
for r in range(1, N + 1):
    for c in range(1, M + 1):
        dp[r][c] = array[r-1][c-1] + (dp[r][c-1] + dp[r-1][c] - dp[r-1][c-1])

for _ in range(int(inp())):
    ar, ac, br, bc = map(int, inp().split())
    print(dp[br][bc] - (dp[br][ac-1] + dp[ar-1][bc] - dp[ar-1][ac-1]))