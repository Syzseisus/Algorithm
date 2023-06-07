import sys

N = int(sys.stdin.readline())

prise = 0
for _ in range(N):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == b:
        if b == c:
            prise = max(prise, 10000 + a * 1000)
        else:
            prise = max(prise, 1000 + a * 100)
    else:
        if b == c:
            prise = max(prise, 1000 + b * 100)
        elif a == c:
            prise = max(prise, 1000 + a * 100)
        else:
            prise = max(prise, max(a, b, c) * 100)

print(prise)
