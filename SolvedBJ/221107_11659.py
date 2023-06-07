from sys import stdin
from collections import defaultdict

N, M = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().rstrip().split()))

DP = [0 for _ in range(N+1)]
DP[1] = arr[0]
for i in range(1, N+1):
    DP[i] = DP[i-1] + arr[i-1]

for _ in range(M):
    i, j = map(int, stdin.readline().split())
    print(DP[j] - DP[i-1])