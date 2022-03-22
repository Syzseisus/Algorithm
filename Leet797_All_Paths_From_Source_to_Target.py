# 0번부터 시작해서 dfs로 하나씩 내려간다
# target에 도달하면 그때까지의 path를 저장하고,
# pop을 통해 하나만 되돌아간다
# ex) 0 -> 1 -> 4 => [0,1,4] 저장, [0,1]에서 재시작


class Solution:
    def allPathsSourceTarget(self, graph):
        answer = []           # 답이 되는 path들을 담을 list
        target = len(graph)-1 # target은 n-1번째 node

        # path를 재귀적으로 하나 씩 더해가는 함수
        def appending(curr):
            if curr == target:              # target에 도달하면
                answer.append(list(path))   # 현재까지의 path를 저장
            else:
                for node in graph[curr]:    # 들어온 node(curr)와 연결된 모든 node를 조사한다
                    path.append(node)       # node를 path에 추가하고
                    appending(node)         # 그 node를 시작으로 path를 또 갱신하러 간다
                    path.pop()              # 갱신이 종료되면 (appending line이 끝나면) pop으로 하나 되돌아간다
                    
        # 0에서 시작한다
        path = [0]
        appending(0)

        return answer
