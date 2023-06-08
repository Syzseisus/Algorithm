import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
DP = [0] * N

answer = 0
for i in range(N):
    DP[i] = 1
    for j in range(i):
        if A[j] < A[i]:
            DP[i] = max(DP[i], DP[j] + 1)
    answer = max(answer, DP[i])

print(answer)
