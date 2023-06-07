import sys

inp = lambda: sys.stdin.readline()

T = int(inp())


for _ in range(T):
    a, b = map(int, inp().rstrip().split())
    answer = pow(a, b, 10)
    answer = answer if answer else 10
    print(answer)