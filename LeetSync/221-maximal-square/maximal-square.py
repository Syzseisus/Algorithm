class Solution:
    def maximalSquare(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        matrix = [[int(matrix[i][j]) for j in range(n)] for i in range(m)]

        if (m == 1) | (n == 1):
            for i in matrix:
                if sum(i): return 1
            return 0

        kl_mat = [[matrix[i][j] if i*j == 0 else 0 for j in range(n)] for i in range(m)]

        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 1:
                    kl_mat[i][j] = min(kl_mat[i-1][j-1], kl_mat[i][j-1], kl_mat[i-1][j]) + 1
                    
        flatten = [kl_mat[i][j] for i in range(m) for j in range(n)]

        return max(flatten) ** 2