import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

sorted_A = sorted(A)
P = [0] * N
for i in range(N):
    P[i] = sorted_A.index(A[i])
    sorted_A[P[i]] = -1

print(*P)
