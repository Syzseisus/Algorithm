import sys

N = int(sys.stdin.readline())

for M in range(max(1, N - 54), N):      # 9 * 6
    if sum(map(int, str(M))) + M == N:
        sys.stdout.write("%d" %M)
        break
else:
    sys.stdout.write("%d" %0)