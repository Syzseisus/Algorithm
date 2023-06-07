import sys
from collections import deque

N = int(sys.stdin.readline())

answers = deque(map(int, sys.stdin.readline().split()))

score = 0
accum = 1
while answers:
    curr = answers.popleft()
    if curr == 1:
        score += accum
        while answers:
            come = answers.popleft()
            if come == 1:
                accum += 1
                score += accum
            else:
                accum = 1
                break

print(score)
