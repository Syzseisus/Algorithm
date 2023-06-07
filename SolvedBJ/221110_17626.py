from sys import stdin
N = int(stdin.readline())

DP = [50001 for i in range(N + 1)]
DP[0] = 0
for i in range(1, N + 1):
    for j in range(1, N + 1):
        val = j  * j
        if val > i:
            break
        DP[i] = min(DP[i], DP[i-val] + 1)

print(DP[-1])