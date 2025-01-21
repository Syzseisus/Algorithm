class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        zero_cols = [False for _ in range(n)]
        flag = False
        for row in matrix:
            if 0 in row:
                for i, r in enumerate(row):
                    if r == 0:
                        zero_cols[i] = True
                        flag = True
                    row[i] = 0

        for i, zero in enumerate(zero_cols):
            if zero:
                for r in range(m):
                    matrix[r][i] = 0