class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # dfs 함수 - 함수 내부에 정의해서 로컬 변수 같이 쓰기
        def dfs(curr):
            # visited[curr] = True
            for ngbr in range(n):
                if isConnected[curr][ngbr] and not visited[ngbr]:
                    visited[ngbr] = True
                    dfs(ngbr)

                if not visited[i]:
                    dfs(i, visited)


        n = len(isConnected)
        visited = [False for _ in range(n)]
        answer = 0
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                answer += 1
                dfs(i)
        
        return answer