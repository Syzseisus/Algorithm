import sys

T = int(sys.stdin.readline())

count = 0
while count < T:
    a = sys.stdin.readline()
    N = int(sys.stdin.readline())
    count += 1

    remain = 0
    for _ in range(N):
        remain += int(sys.stdin.readline())
        _, remain = divmod(remain, N)

    if not remain:
        print("YES")
    else:
        print("NO")
