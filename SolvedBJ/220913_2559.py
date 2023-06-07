import sys
from collections import deque

inp = lambda: sys.stdin.readline()

N, K = map(int, inp().rstrip().split())
temperature = list(map(int, inp().rstrip().split()))

Q = deque(temperature[:K])
sum_ = sum(Q)
max_ = sum_
for i in range(K, N):
    temp = sum_
    prev = Q.popleft()
    next = temperature[i]
    temp += (next - prev)

    Q.append(next)
    sum_ = temp
    max_ = max(max_, temp)

print(max_)