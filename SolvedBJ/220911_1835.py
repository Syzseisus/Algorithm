import sys
from collections import deque

inp = lambda: int(sys.stdin.readline())

N = inp()

dq = deque([N])

card = N - 1
while card:
    for _ in range(card + 1):
        dq.appendleft(dq.pop())
    dq.appendleft(card)
    card -= 1

dq.appendleft(dq.pop())
print(*dq)

# "deque.rotate(n)"
# = n번 회전한다
# ex) deque([1,2,3,4,5]).rotate(2)
#     => deque([4,5,1,2,3])