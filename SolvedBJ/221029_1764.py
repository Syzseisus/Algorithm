from sys import stdin
import heapq

N, M = map(int, stdin.readline().split())
non_hear = set()
for _ in range(N):
    non_hear.add(stdin.readline().rstrip())

non_hear_see = []
for _ in range(M):
    name = stdin.readline().rstrip()
    if name in non_hear:
        non_hear_see.append(name)

heapq.heapify(non_hear_see)
print(len(non_hear_see))
while non_hear_see:
    print(heapq.heappop(non_hear_see))
