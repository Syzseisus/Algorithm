import sys
from collections import deque


inp = lambda: sys.stdin.readline()


def hack(keylog):
    left = deque()
    right = deque()
    for k in keylog:
        if k == '<':
            if left:
                right.appendleft(left.pop())
        elif k == '>':
            if right:
                left.append(right.popleft())
        elif k == '-':
            if left:
                left.pop()
        else:
            left.append(k)

    print(''.join(left) + ''.join(right))


T = int(inp())
for _ in range(T):
    keylog = inp().strip()
    hack(keylog)
