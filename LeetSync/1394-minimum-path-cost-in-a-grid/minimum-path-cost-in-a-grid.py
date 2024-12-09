"""
5 1 2
4 0 3

0 - 12, 10, 15 : 안 씀
1 - 20, 23,  8 : 1->4, 1->0, 1->3
2 - 21,  7,  1 : 2->4, 2->0, 2->3
3 -  8,  1, 13 : 안 씀
4 -  9, 10, 25 : 안 씀
5 -  5,  3,  2 : 5->4, 5->0, 5->3

5 -> 4 : 5 +  5 + 4 = 14
5 -> 0 : 5 +  3 + 0 =  8
5 -> 3 : 5 +  2 + 3 = 10
1 -> 4 : 1 + 20 + 4 = 25
1 -> 0 : 1 + 23 + 0 = 24
1 -> 3 : 1 +  8 + 3 = 12
2 -> 4 : 2 + 21 + 4 = 27
2 -> 0 : 2 +  7 + 0 =  9
2 -> 3 : 2 +  1 + 3 =  6
답은 6
"""

class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        # 0층부터 시작
        prev = grid[0]
        for r in range(1, rows):
            # 다음 층에 도착했을 때 dp 결과 (그 cell에 도달하는 min cost)
            curr = [float('inf') for _ in range(cols)] 
            for i in range(cols):
                for j in range(cols):
                    # 누적되어야 할 값은 다음과 같이 `현재 누적 + 이동 + 다음 cell 값`
                    step = (
                        prev[i]             # 1. 이전 층 cell에 누적된 값
                        + moveCost[         # 2. 이동 비용인데
                            grid[r - 1][i]  #   from : 이전 층 cell의 index
                        ][j]                #   to   : 다음 층의 j번째 cell
                        + grid[r][j]        # 3. 다음 층 cell의 j번째 cell의 index == 다음 cell 값
                    )
                    # 이전 층의 몇 번째 cell에서
                    # 다음 층의 j번째 cell로 이동하는 게 최소인지 계산하게 됨
                    curr[j] = min(curr[j], step)
            
            # 다음 층으로 이동
            prev = curr
        
        # 마지막 층에서 최솟값이 정답임
        return min(prev)
        
        
        
        
        
        
        
        
        
        
        
        
        
        