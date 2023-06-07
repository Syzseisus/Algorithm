import sys

inp = lambda: sys.stdin.readline().strip().split()

N, M = map(int, inp())
A = [list(map(int, inp())) for _ in range(N)]
M, K = map(int, inp())
B = [list(map(int, inp())) for _ in range(M)]

# print(A)
# print(B)

C = [[0] * K for _ in range(N)]
for i in range(N):
    for j in range(M):
        for k in range(K):
            C[i][k] += A[i][j] * B[j][k]

for row in C:
    print(*row)