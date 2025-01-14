class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        def supporter(nums):
            n = len(nums)
            if n == 1:
                return nums
            a, b = divmod(n, 2)
            new_n = a + b
            new_nums = [None for _ in range(new_n)]
            for i in range(0, new_n, 2):
                new_nums[i] = min(nums[2 * i], nums[2 * i + 1])
            for i in range(1, new_n, 2):
                new_nums[i] = max(nums[2 * i], nums[2 * i + 1])
            return supporter(new_nums)

        return supporter(nums)[0]
