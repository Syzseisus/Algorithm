from collections import deque


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        N = len(arr)

        def bfs(start_ind):
            queue = deque([start_ind])
            visited = set()
            while queue:
                curr_ind = queue.pop()
                
                if curr_ind < 0:
                    continue
                elif curr_ind >= N:
                    continue
                elif arr[curr_ind] == 0:
                    return True
                
                if curr_ind in visited:
                    continue
                visited.add(curr_ind)
                
                queue.append(curr_ind + arr[curr_ind])
                queue.append(curr_ind - arr[curr_ind])

            return False

        return bfs(start)