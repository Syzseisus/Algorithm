import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())

comb = combinations(range(1, N + 1), M)
for c in comb:
    print(*c)
