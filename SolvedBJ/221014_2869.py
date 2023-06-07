import sys

A, B, V = map(int, sys.stdin.readline().rstrip().split())
print((V - A - 1) // (A - B) + 2)