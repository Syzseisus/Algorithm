import sys

inp = lambda: sys.stdin.readline()

t = int(inp())

for _ in range(t):
    a, b = map(int, inp().split())
    c = a + b + 1 if 2 <= (a + b) <= 49 else a + b - 49 if 50 <= (a + b) <= 99 else 50
    print(c)