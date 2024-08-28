from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        if len(nums) == 2:
            return nums
        
        answer = []
        for k, v in Counter(nums).items():
            if v == 1:
                answer.append(k)
        
        return answer