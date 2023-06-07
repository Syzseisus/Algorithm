import sys

inp = lambda: sys.stdin.readline()

T = int(inp())
for _ in range(T):
    V, E = map(int, inp().strip().split())
    print(2 - V + E)