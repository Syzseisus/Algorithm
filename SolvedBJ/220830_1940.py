import sys
from collections import deque as dq

inp = lambda: sys.stdin.readline()

N = int(inp())
M = int(inp())
elems = list(map(int, inp().strip().split()))
elems.sort()
elems = dq(elems)

answer = 0
if N != 1:
    l = 0
    r = N - 1
    
    while l < r:
        low = elems[l]
        high = elems[r]
        cand = low + high

        if cand > M:
            r -= 1
            continue
        elif cand < M:
            l += 1
            continue
        elif cand == M:
            answer += 1
            l += 1
            r -= 1
    
print(answer)