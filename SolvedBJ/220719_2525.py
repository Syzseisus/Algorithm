import sys

H, M = map(int, sys.stdin.readline().split())
spend = int(sys.stdin.readline())

M += spend
if M >= 60:
    add_H, M = divmod(M, 60)
    H += add_H
if H >= 24:
    _, H = divmod(H, 24)

print(H, M)
