import sys
from itertools import combinations_with_replacement as comb

_, M = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
array.sort()

for p in comb(array, r=M):
    print(*p)
