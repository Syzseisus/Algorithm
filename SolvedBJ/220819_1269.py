import sys

inp = lambda: sys.stdin.readline()

na, nb = map(int, inp().split())
A = set(inp().strip().split())
B = set(inp().strip().split())
cup = A.intersection(B)
print(na + nb - 2 * len(cup))