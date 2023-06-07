import sys

inp = lambda: sys.stdin.readline()

T = int(inp())
for _ in range(T):
    A, B = map(int, inp().rstrip().split())
    print(A + B)