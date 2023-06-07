import sys

N, K = map(int, sys.stdin.readline().split())

pascal = [[1 for _ in range(min(i, K + 1))] for i in range(1, N + 2)]

for n in range(2, N + 1):
    for r in range(1, min(n, K + 1)):
        pascal[n][r] = pascal[n-1][r-1] + pascal[n-1][r]

print(pascal[N][K])