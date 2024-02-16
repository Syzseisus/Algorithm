'''
DP[i] = max(DP[i-1], DP[i-2], ..., DP[i-k+1]) + nums[i]
'''
# class Solution:
#     def maxResult(self, nums: List[int], k: int) -> int:
#         n = len(nums)
#         D = [-float('inf')] * (n)
#         heap = [(-nums[0], 0)]
#         D[0] = nums[0]   
#         for i in range(1,n):
#             (maxValue, index) = heap[0]            
#             while index < i - k:
#                 heapq.heappop(heap)
#                 (maxValue, index) = heap[0]

#             D[i] = -maxValue + nums[i]
#             heapq.heappush(heap, (-D[i], i))

#         return D[n-1]
import heapq as hq
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        DP = [-1e5 for _ in nums]
        DP[0] = nums[0]

        heap = [(-nums[0], 0)]
        for i in range(1, len(nums)):
            max_, ind = heap[0]
            while ind < i - k:
                hq.heappop(heap)
                max_, ind = heap[0]

            DP[i] = -max_ + nums[i]
            hq.heappush(heap, (-DP[i], i))
        
        return DP[-1]