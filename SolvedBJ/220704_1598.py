import sys

a, b = map(int, sys.stdin.readline().split())

a_c, a_r = divmod((a - 1), 4)
b_c, b_r = divmod((b - 1), 4)

print(abs(b_r - a_r) + abs(b_c - a_c))
