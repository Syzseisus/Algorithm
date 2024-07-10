class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])
        diag = n + m

        cnt = 0
        trav = []
        for i in range(diag):
            sub = []
            for row in range(n):
                col = i - row
                if col >= 0 and col < m:
                    # print(i, row, col)
                    sub.append(mat[row][col])
            if cnt:
                trav.extend(sub)
            else:
                trav.extend(sub[::-1])
            cnt = 1 - cnt

        return trav