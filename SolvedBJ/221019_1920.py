from sys import stdin

N = int(stdin.readline())
A = set(map(int, stdin.readline().strip().split()))
M = int(stdin.readline())
B = list(map(int, stdin.readline().strip().split()))

for b in B:
    print(int(b in A))