from sys import stdin

N = int(stdin.readline())
stairs = [0] + [int(stdin.readline()) for _ in range(N)]
if N == 1:
    answer = stairs[1]
elif N == 2:
    answer = sum(stairs)
else:
    DP = [0] * (N + 1)
    DP[1] = stairs[1]
    DP[2] = stairs[1] + stairs[2]
    DP[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

    for i in range(4, N + 1):
        DP[i] = max(
            DP[i-3] + stairs[i-1] + stairs[i],
            DP[i-2] + stairs[i]
        )
    answer = DP[-1]
print(answer)