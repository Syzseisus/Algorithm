import sys

M = int(sys.stdin.readline())
ball = {1: True, 2: False, 3: False}

for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    if a == b:
        continue
    else:
        ball[a], ball[b] = ball[b], ball[a]

answer = [k for k in ball if ball[k]]
print(*answer)
