import sys
import heapq as hq
from itertools import permutations

inp = lambda: sys.stdin.readline()

T = int(inp())
nums = [int(inp().strip()) for _ in range(T)]
nums.sort()
nums = nums[:4]

cands = []
for pair in permutations(nums, 2):
    hq.heappush(cands, int(str(pair[0]) + str(pair[1])))

# print(cands)

hq.heappop(cands)
hq.heappop(cands)

print(cands[0])