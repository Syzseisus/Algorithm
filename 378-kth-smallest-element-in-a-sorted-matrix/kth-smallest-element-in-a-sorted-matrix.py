import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        low = matrix[0][0]
        high = matrix[-1][-1]

        while low <= high:
            mid = (high - low) // 2 + low
            cnt = 0
            ans = low

            for i in range(n):
                j = n - 1
                while j >= 0 and matrix[i][j] > mid:
                    j -= 1
                if j >= 0:
                    cnt += 1 + j
                    ans = max(ans, matrix[i][j])
                else:
                    break

            if cnt == k:
                return ans
            elif cnt < k:
                low = mid + 1
            else:
                high = mid - 1
        
        return low