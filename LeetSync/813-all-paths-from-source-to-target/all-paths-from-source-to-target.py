class Solution:
    def allPathsSourceTarget(self, graph):
        answer = []
        target = len(graph)-1

        def appending(curr):
            if curr == target:
                answer.append(list(path))
            else:
                for node in graph[curr]:
                    path.append(node)
                    appending(node)
                    path.pop()
                    
        path = [0]
        appending(0)

        return answer