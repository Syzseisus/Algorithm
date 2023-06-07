import sys
import heapq as hq

arr = []
for _ in range(int(sys.stdin.readline())):
    hq.heappush(arr, int(sys.stdin.readline()))

while arr:
    print(hq.heappop(arr))