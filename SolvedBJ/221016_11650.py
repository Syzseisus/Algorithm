import sys
arr = [list(map(int, sys.stdin.readline().rstrip().split()))
       for _ in range(int(sys.stdin.readline()))]
arr.sort()
for i in arr:
    print(*i)