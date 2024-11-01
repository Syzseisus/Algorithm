class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        x = range(1, len(nums) + 1)
        nums = set(nums)
        answer = []
        for i in x:
            if i not in nums:
                answer.append(i)
        
        return answer