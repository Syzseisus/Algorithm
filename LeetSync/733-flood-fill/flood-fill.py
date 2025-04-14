'''
2 1 2
1 2 0
2 0 2
'''

from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        target = image[sr][sc]

        image[sr][sc] = color

        queue = deque([(sr, sc)])
        while queue:
            cr, cc = queue.popleft()
            for i, j in [(-1, 0), (+1, 0), (0, -1), (0, +1)]:
                if ((cr + i) >= m) or ((cc + j) >= n) or ((cr + i) < 0) or ((cc + j) < 0):
                    continue
                ngbr_color = image[cr + i][cc + j]
                if ngbr_color == target and not visited[cr + i][cc + j]:
                    image[cr + i][cc + j] = color
                    queue.append((cr + i, cc + j))
                    visited[cr + i][cc + j] = True
        
        return image