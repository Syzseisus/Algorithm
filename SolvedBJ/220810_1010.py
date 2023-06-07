import sys

inp = lambda: sys.stdin.readline()

T = int(inp())
# 모든 테스트 케이스에서 가장 큰 M을 기준으로 memo한다
large_M = 0
answer_NM = []
for _ in range(T):
    N, M = map(int, inp().split())
    # 답 해야 하는 경우 저장
    answer_NM.append((M, N))
    large_M = max(large_M, M)

# 하삼각행렬 정의: DP[n][k] == nCk
DP = [[0 for _ in range(i + 1)] for i in range(M + 1)]
for n in range(M + 1):
    for k in range(n + 1):
        # nC0 = 1
        if k == 0:
            DP[n][k] = 1
        # nC1 = n
        elif k == 1:
            DP[n][k] = n
        # nCk = nCn-k
        elif DP[n][n-k]:
            DP[n][k] = DP[n][n-k]
        # nCk = n-1Ck-1 + n-1Ck 
        else:
            DP[n][k] = DP[n-1][k-1] + DP[n-1][k]

# for i in DP:
#     print(*i)

for M, N in answer_NM:
    print(DP[M][N])
