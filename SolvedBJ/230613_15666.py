import sys
from itertools import combinations_with_replacement as comb

_, M = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
array.sort()

pairs = set(comb(array, M))
pairs = sorted(pairs)

for p in pairs:
    print(*p)
