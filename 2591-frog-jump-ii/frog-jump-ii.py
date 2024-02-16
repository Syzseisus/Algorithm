class Solution:
    def maxJump(self, stones: List[int]) -> int:
        total = len(stones)
        if total == 2:
            return stones[1] - stones[0]
        else:
            go = max(stones[i+2] - stones[i] for i in range(0, total-2))
            back = max(stones[i+1] - stones[i] for i in range(1, total-1))

            return max(go, back)