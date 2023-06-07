N = int(input())
if N == 1:
    print(0)
elif N == 2:
    print(1)
elif N == 3:
    print(1)
else:
    DP = [0] * (N + 1)
    DP[1] = 0
    DP[2] = 1
    DP[3] = 1
    for i in range(4, N + 1):
        if (i % 3 == 0) and (i % 2 == 0):
            DP[i] = min(DP[i//2], DP[i//3], DP[i-1]) + 1
        elif i % 3 == 0:
            DP[i] = min(DP[i//3], DP[i-1]) + 1
        elif i % 2 == 0:
            DP[i] = min(DP[i//2], DP[i-1]) + 1
        else:
            DP[i] = DP[i-1] + 1
    print(DP[-1])
