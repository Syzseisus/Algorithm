import sys

N, M, K = map(int, sys.stdin.readline().strip().split())

comb = [[0 for _ in range(i + 1)] for i in range(N + 1)]

for i in range(N + 1):
    comb[i][0] = 1
    comb[i][i] = 1
    try:
        for j in range(1, i):
            comb[i][j] = comb[i-1][j-1] + comb[i-1][j]
    except:
        continue

answer = 0
while M >= K:
    if (N - M) < (M - K):
        K += 1
        continue

    answer += comb[M][K] * comb[N-M][M-K] / comb[N][M]
    K += 1

print(answer)