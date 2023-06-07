import sys
import heapq as hq
from collections import defaultdict

inp = lambda: sys.stdin.readline()

N, D = map(int, inp().split())

highway = [[] for _ in range(D + 1)]
for i in range(D):
    highway[i].append((i+1, 1))

for _ in range(N):
    src, tgt, dst = map(int, inp().split())
    if tgt > D:
        continue
    highway[src].append((tgt, dst))

distances = [float('inf')] * (D + 1)
distances[0] = 0

q = []
hq.heappush(q, (0, 0))
while q:
    curr_dst, curr = hq.heappop(q)
    if distances[curr] < curr_dst:
        continue
    
    for next in highway[curr]:
        cost = curr_dst + next[1]
        if distances[next[0]] > cost:
            distances[next[0]] = cost
            hq.heappush(q, (cost, next[0]))

print(distances[-1])