class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        
        answer = 0
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    continue
                    
                flag = True
                for r2 in range(m):
                    if r != r2 and mat[r2][c] == 1:
                        flag = False
                        break
                
                for c2 in range(n):
                    if c != c2 and mat[r][c2] == 1:
                        flag = False
                        break
                
                if flag:
                    answer += 1
        
        return answer
