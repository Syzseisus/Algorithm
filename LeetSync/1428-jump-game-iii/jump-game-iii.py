class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        N = len(arr)
        
        queue = [start]
        # visited = set()
        visited = 0

        while queue:
            curr_ind = queue.pop()
            # visited.add(curr_ind)
            visited |= (1 << curr_ind)

            left_ind = curr_ind - arr[curr_ind]
            if 0 <= left_ind < N:
                if arr[left_ind] == 0:
                    return True
                # elif left_ind not in visited:
                elif not visited & (1 << left_ind):
                    queue.append(left_ind)

            right_ind = curr_ind + arr[curr_ind]
            if 0 <= right_ind < N:
                if arr[right_ind] == 0:
                    return True
                # elif right_ind not in visited:
                elif not visited & (1 << right_ind):
                    queue.append(right_ind)
        
        return False
        
        
        
#         N = len(arr)

#         def bfs(start_ind):
#             queue = [start_ind]
#             visited = set()
#             while queue:
#                 curr_ind = queue.pop()
                
#                 if curr_ind in visited:
#                     continue
#                 visited.add(curr_ind)
                
#                 if curr_ind < 0:
#                     continue
#                 elif curr_ind >= N:
#                     continue
#                 elif arr[curr_ind] == 0:
#                     return True
                
#                 queue.append(curr_ind + arr[curr_ind])
#                 queue.append(curr_ind - arr[curr_ind])

#             return False

#         return bfs(start)