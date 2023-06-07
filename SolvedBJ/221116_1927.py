from sys import stdin
import heapq as hq

arr = []
N = int(stdin.readline())
for _ in range(N-1):
    x = int(stdin.readline())
    if x == 0:
        try:
            print(hq.heappop(arr))
        except:
            print(0)
    else:
        hq.heappush(arr, x)

x = int(stdin.readline())
if x == 0:
    try:
        print(hq.heappop(arr))
    except:
        print(0)