import sys
from itertools import combinations_with_replacement as comb_r

N, M = map(int, sys.stdin.readline().split())
comb = comb_r(range(1, N + 1), M)
for c in comb:
    print(*c)
