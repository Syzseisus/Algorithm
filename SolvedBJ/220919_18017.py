import sys
c = 299792458

A, B = map(float, sys.stdin.readline().rstrip().split())

print(f"{(A + B) / (1 + (A * B) / (c ** 2)):.2f}")