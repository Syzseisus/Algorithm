from collections import defaultdict as ddict
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        helper = ddict(int)
        for n in nums:
            helper[n] += 1
        # print(helper)
        k = len(helper)
        
        n = -100
        i = 0
        while i < k:
            # print('ㅁ', i, n)
            if n in helper:
                # print("H")
                nums[i] = n
                i += 1
            n += 1
        print(nums)
        for i in range(k, len(nums)):
            nums[i] = "_"
        return k