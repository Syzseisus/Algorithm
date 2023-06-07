import sys
from collections import deque as dq

inp = lambda: sys.stdin.readline()

left = dq(inp().strip())
cursor = len(left)
right = dq()

M = int(inp())
for _ in range(M):
    command = dq(inp().strip().split())
    if command[0] == "L" and left:
        right.appendleft(left.pop())
    elif command[0] == "D" and right:
        left.append(right.popleft())
    elif command[0] == "B" and left:
        left.pop()
    elif command[0] == "P":
        left.append(command[1])

answer = ''.join(left + right)
print(answer)