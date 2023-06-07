import sys
from itertools import permutations

_, M = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
array.sort()

perm = permutations(array, M)
for p in perm:
    print(*p)
