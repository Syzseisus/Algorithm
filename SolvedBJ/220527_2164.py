from collections import deque

N = int(input())
queue = deque([i + 1 for i in range(N)])

while len(queue) > 1:
    queue.popleft()
    if len(queue) == 1:
        break
    temp = queue.popleft()
    queue.append(temp)

print(queue[0])
