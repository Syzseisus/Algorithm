import sys

N = int(sys.stdin.readline())
triangle = []
for _ in range(N):
    triangle.append(list(map(int, sys.stdin.readline().split())))

DP = [[0 for _ in range(i)] for i in range(1, N + 1)]

for j in range(N):
    if not j:
        DP[j][0] = triangle[0][0]
    else:
        DP[j][0] = DP[j - 1][0] + triangle[j][0]
        DP[j][j] = DP[j - 1][j - 1] + triangle[j][j]

    for k in range(1, j):
        DP[j][k] = triangle[j][k] + max(DP[j - 1][k - 1], DP[j - 1][k])

print(max(DP[-1]))
