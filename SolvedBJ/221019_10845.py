from sys import stdin
from collections import deque

Q = deque()
for _ in range(int(stdin.readline())):
    order = list(stdin.readline().split())
    if order[0] == 'push':
        Q.appendleft(int(order[1]))
    elif order[0] == 'pop':
        print(Q.pop() if Q else -1)
    elif order[0] == 'size':
        print(len(Q))
    elif order[0] == 'empty':
        print(0 if Q else 1)
    elif order[0] == 'front':
        print(Q[-1] if Q else -1)
    elif order[0] == 'back':
        print(Q[0] if Q else -1)