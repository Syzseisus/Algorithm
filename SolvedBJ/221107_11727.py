from sys import stdin
N = int(stdin.readline())

if N == 1:
    print(1)
elif N == 2:
    print(3)
else:
    DP = [0] * N
    DP[0] = 1
    DP[1] = 3
    for i in range(2, N):
        DP[i] = (DP[i-1] + 2 * DP[i-2]) % 10007

    print(DP[-1])