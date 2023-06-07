import sys

N, K = map(int, sys.stdin.readline().split())

answer = 0
while bin(N).count('1') > K:
    ind = bin(N)[:1:-1].index('1')
    answer += 2 ** ind
    N += 2 ** ind

print(answer)