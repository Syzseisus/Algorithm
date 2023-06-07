import sys

inp = lambda: sys.stdin.readline()

N = int(inp())
A = list(map(int, inp().split()))
B = list(map(int, inp().split()))
A.sort()

S = 0
for i in range(N):
    S += A[i] * B.pop(B.index(max(B)))

print(S)
