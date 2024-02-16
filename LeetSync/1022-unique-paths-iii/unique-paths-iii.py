class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        end_state = 0
        for r in range(m):
            for c in range(n):
                ind = r * n + c
                if grid[r][c] != -1:
                    end_state |= (1 << ind)
                
                if grid[r][c] == 1:
                    start_state = 1 << ind
                    sr, sc = r, c

        answer = 0
        def dfs(r, c, state):
            nonlocal answer

            if grid[r][c] == 2:
                if state == end_state:
                    answer += 1
                return

            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr = r + dr
                nc = c + dc
                ind = nr * n + nc
                if ((0 <= nr < m and 0 <= nc < n) and
                    ((1 << ind) & state == 0) and
                    grid[nr][nc] != -1):
                    dfs(nr, nc, state | (1 << ind))

        dfs(sr, sc, start_state)

        return answer