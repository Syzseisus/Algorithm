import sys

N = int(sys.stdin.readline())

print(bin(N)[2:].count('1'))