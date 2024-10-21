class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        digit = len(nums[0])
        appear = set(nums)
        for decimal in range(2 ** digit):
            binary = str(bin(decimal))[2:].rjust(digit, '0')
            if binary not in appear:
                return binary
