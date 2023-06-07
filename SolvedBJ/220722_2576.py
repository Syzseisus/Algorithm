import sys

odds = []
for i in range(7):
    N = int(sys.stdin.readline())
    if N % 2:
        odds.append(N)

if odds:
    print(sum(odds))
    print(min(odds))
else:
    print(-1)
