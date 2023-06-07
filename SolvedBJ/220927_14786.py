import sys
import math

A, B, C = map(int, sys.stdin.readline().strip().split())

fx = lambda x: A * x + B * math.sin(x) - C
dx = lambda x: A + B * math.cos(x)

x = 0
while abs(fx(x)) >= 1e-9:
    x -= fx(x) / dx(x)

print(x)