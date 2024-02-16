import operator as op
from functools import reduce

class Solution:
    def uniquePathsWithObstacles(self, og: List[List[int]]) -> int:
        # if og[0][0] == 1 or og[-1][-1] == 1:
        #     return 0
        
        ROW = len(og)
        COL = len(og[0])
        
        # if ROW == 1:
        #     return 0 if any(og[0]) else 1
        # elif COL == 1:
        #     for r in range(ROW):
        #         if og[r][0]:
        #             return 0
        #     else:
        #         return 1
        
        
        euler = [[0 for _ in range(COL)] for _ in range(ROW)]
                
        for r in range(ROW):
            if og[r][0] == 0:
                euler[r][0] = 1
            else:
                break

        for c in range(COL):
            if og[0][c] == 0:
                euler[0][c] = 1
            else:
                break
                
        for r in range(1, ROW):
            for c in range(1, COL):
                if og[r][c] == 0:
                    euler[r][c] = euler[r - 1][c] + euler[r][c - 1]
        
        
        return euler[-1][-1]