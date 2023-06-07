import sys
from collections import deque

N, K = map(int, sys.stdin.readline().rstrip().split())

Q = deque(range(1, N + 1))

answer = []
while Q:
    for _ in range(K - 1):
        Q.append(Q.popleft())
    answer.append(Q.popleft())

print("<", end='')
for i in range(N - 1):
    print(f"{answer[i]}, ", end='')
print(f"{answer[-1]}>")