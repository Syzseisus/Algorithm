from sys import stdin

N = int(stdin.readline())
arr = list(map(int, stdin.readline().rstrip().split()))
SG = dict()
for i in arr:
    SG[i] = SG.get(i, 0) + 1
M = int(stdin.readline())
cards = list(map(int, stdin.readline().strip().split()))
for i in cards:
    print(SG.get(i, 0), end=' ')
print()