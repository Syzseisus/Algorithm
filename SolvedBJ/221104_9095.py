from sys import stdin

DP = [0] * 11   # 0 ~ 10
DP[1] = 1
DP[2] = 2
DP[3] = 4
def combine_ott(N):
    for i in range(4, N + 1):
        if DP[i] == 0:
            DP[i] = DP[i-1] + DP[i-2] + DP[i-3]

    return DP[N]

for _ in range(int(stdin.readline())):
    print(combine_ott(int(stdin.readline())))