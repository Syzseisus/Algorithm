from sys import stdin
from functools import reduce
from collections import defaultdict

def solution(clothes):
    hash_closet = defaultdict(lambda: 1)
    for c in clothes:
        hash_closet[c[1]] += 1
    lengths = list(hash_closet.values())
    
    return reduce(lambda x, y: x * y, lengths) - 1

for _ in range(int(stdin.readline())):
    N = int(stdin.readline())
    if N == 0:
        print(0)
    elif N == 1:
        _ = stdin.readline()
        print(1)
    else:
        clothes = [stdin.readline().rstrip().split() for _ in range(N)]
        # print(clothes)
        print(solution(clothes))
