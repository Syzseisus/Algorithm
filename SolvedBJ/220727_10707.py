import sys


def water(B, C, D, P):
    if P <= C:
        return B
    else:
        return B + (P - C) * D


A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())
D = int(sys.stdin.readline())
P = int(sys.stdin.readline())

X = P * A
Y = water(B, C, D, P)
answer = min(X, Y)

print(answer)
