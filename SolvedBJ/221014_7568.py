import sys

arr = [list(map(int, sys.stdin.readline().rstrip().split()))
       for _ in range(int(sys.stdin.readline()))]

for i in arr:
    rank = 1
    for j in arr:
        if i == j:
            continue
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=' ')
print()