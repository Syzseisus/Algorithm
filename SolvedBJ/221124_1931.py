import heapq
from sys import stdin

N = int(stdin.readline())
meets = []
for _ in range(N):
    s, e = map(int, stdin.readline().rstrip().split())
    heapq.heappush(meets, (e, s))
# meets.sort(key=lambda x: x[1])
# print(meets)

cnt = 1
prev_e, prev_s = heapq.heappop(meets)
while meets:
    curr_e, curr_s = heapq.heappop(meets)
    if curr_s < prev_e:
        continue
    else:
        # print(f"({curr_s}, {curr_e})")
        prev_e, prev_s = curr_e, curr_s
        cnt +=1
print(cnt)