import sys
from collections import deque


def rotate(a):
    if deq[0] == a:
        deq.popleft()
        return 0
    else:
        remain = len(deq)
        pos = deq.index(a)
        if pos <= remain // 2:
            res = 0
            while True:
                temp = deq.popleft()
                if temp == a:
                    return res
                else:
                    res += 1
                    deq.append(temp)
        else:
            res = 1
            while True:
                temp = deq.pop()
                if temp == a:
                    return res
                else:
                    res += 1
                    deq.appendleft(temp)


N, _ = map(int, sys.stdin.readline().split())
deq = deque(range(1, N + 1))

answer = 0
want_to_pop = map(int, sys.stdin.readline().split())
for i in want_to_pop:
    answer += rotate(i)

print(answer)
