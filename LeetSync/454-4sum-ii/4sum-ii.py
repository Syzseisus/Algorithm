from collections import defaultdict as ddict

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # 아이디어: 둘씩 나눠서, nums1[i] + nums2[j] == -(nums3[k] + nums4[l]) 찾기
        left = ddict(lambda: 0)
        for n1 in nums1:
            for n2 in nums2:
                left[n1 + n2] += 1
        
        ans = 0
        for n3 in nums3:
            for n4 in nums4:
                ans += left[-(n3 + n4)]

        return ans