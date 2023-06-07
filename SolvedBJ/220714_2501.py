import sys

N, K = map(int, sys.stdin.readline().split())

count = 0
for i in range(1, N + 2):
    if N % i == 0:
        count += 1
    if count == K:
        print(i)
        break
    if i == N + 1:
        print(0)
