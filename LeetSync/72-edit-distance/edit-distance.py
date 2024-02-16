class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N = len(word1)
        M = len(word2)

        DP = [[-1 for _ in range(N+1)] for _ in range(M+1)]

        for i in range(N+1):
            DP[0][i] = i
        for i in range(M+1):
            DP[i][0] = i

        for j in range(1, M+1):
            for i in range(1, N+1):
                if word1[i-1] == word2[j-1]:
                    DP[j][i] = DP[j-1][i-1]
                else:
                    insert = DP[j-1][i]
                    delete = DP[j][i-1]
                    replace = DP[j-1][i-1]
                    DP[j][i] = min(insert, delete, replace) + 1

        return DP[M][N]