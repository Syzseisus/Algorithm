from sys import stdin
from collections import deque

for _ in range(int(stdin.readline())):
    N, M = map(int, stdin.readline().rstrip().split())
    Q = deque(map(int, stdin.readline().rstrip().split()))
    indices = deque([False] * N)
    indices[M] = True

    count = 0
    curr_max = max(Q)
    while True:
        if Q[0] == curr_max:
            count += 1

            if indices[0]:
                print(count)
                break
            else:
                Q.popleft()
                indices.popleft()
                curr_max = max(Q)

        else:
            Q.append(Q.popleft())
            indices.append(indices.popleft())
