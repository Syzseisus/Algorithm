import sys


def fib(N):
    DP = [0] * (N + 1)
    DP[1] = 1
    for i in range(2, N + 1):
        DP[i] = DP[i - 1] + DP[i - 2]
    return DP[N - 1], DP[N]


T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    if N == 0:
        print(1, 0)
    elif N == 1:
        print(0, 1)
    else:
        a, b = fib(N)
        print(a, b)
