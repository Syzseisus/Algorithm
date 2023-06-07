import sys
arr = [list(map(int, sys.stdin.readline().rstrip().split()))
       for _ in range(int(sys.stdin.readline()))]
arr.sort(key=lambda x: (x[1], x[0]))
for i in arr:
    print(*i)