import heapq as hq
from sys import stdin

arr = []
for _ in range(int(stdin.readline())):
    x = int(stdin.readline())
    if x == 0:
        if arr:
            print(hq.heappop(arr)[1])
        else:
            print(0)
    else:
        hq.heappush(arr, (abs(x), x))