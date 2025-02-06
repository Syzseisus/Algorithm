# class Solution:
#     def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
#         col = 0
#         for num in nums:
#             col = max(len(num), col)

#         answer = []
#         for d in range(len(nums) + col - 1):
#             temp = []
#             for i, row in enumerate(nums):
#                 if i > d:
#                     continue
#                 try:
#                     temp.append(row[d - i])
#                 except:
#                     continue
#             temp = temp[::-1]
#             answer.extend(temp)
#         return answer


from collections import defaultdict
from typing import List

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diagonal_map = defaultdict(list)
        
        # 각 (i, j) 위치의 요소를 i + j를 key로 하여 저장
        for i, row in enumerate(nums):
            for j, val in enumerate(row):
                diagonal_map[i + j].append(val)
        
        answer = []
        
        # 대각선 순서대로 리스트를 병합
        for key in sorted(diagonal_map.keys()):  
            answer.extend(reversed(diagonal_map[key]))  # 역순 추가
        
        return answer
