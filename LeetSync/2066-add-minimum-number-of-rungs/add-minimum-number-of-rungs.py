class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        ans = 0

        left = 0
        for num in rungs:
            cur_dist = num - left
            left = num

            if cur_dist <= dist:
                continue
            
            ladder = (cur_dist - 1) // dist
            # print(ladder, cur_dist)
            ans += ladder
        
        return ans
        