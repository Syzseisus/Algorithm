from heapq import *

class Solution:
    def trapRainWater(self, heightMap):
        # variable 설정
        row, col = len(heightMap), len(heightMap[0])    # 행, 열 크기
        heap = []                                       # minHeap을 위한 heap list
        visited = [[0]*col for _ in range(row)]         # 한 번 간 곳은 다시 안 감
        trapped = 0                                     # 정답

        # 1. 예외처리
        #    - 행이나 열이 2개 이하이면 다른 하나가 얼마나 길든 trap 불가능
        if (row <= 2) or (col <= 2): return 0

        # 2. heap 초기 설정
        #    1) 가장자리에 대한 (값, 인덱스) 쌍 push
        #    2) visited = 1
        #       - 여기는 빗물이 찰 수 없기 때문에 방문할 필요가 없음
        for m in range(row):
            for n in range(col):
                if (m*n == 0) or (m == row-1) or (n == col-1):
                    heappush(heap, (heightMap[m][n], m, n))
                    visited[m][n] = 1       

        # 3. 반복
        #   - heap이 남아 있는 동안 반복
        while heap:
            # 1) 제일 낮은 값 pop
            height, m, n = heappop(heap)
            
            # 2) pop한 값에 대한 위, 아래, 왼쪽, 오른쪽 인덱스
            tblr = [(m-1, n), (m+1, n), (m, n-1), (m, n+1)]
            for i, j in tblr:
                # 3) 방문하지 않은 유효한 인덱스에만 접근
                valid_index = (0 <= i < row) and (0 <= j < col)
                if valid_index and (not visited[i][j]):
                    # 4) 방문 안했으니까 넣고
                    heappush(heap, (max(heightMap[i][j], height), i, j))

                    # 5) 정답과 visisted update
                    trapped += max(0, height - heightMap[i][j])
                    visited[i][j] = 1

        return trapped