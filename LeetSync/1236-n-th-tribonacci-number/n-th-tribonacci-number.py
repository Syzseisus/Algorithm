from collections import deque

class Solution:
    def tribonacci(self, n: int) -> int:
        init = deque([0, 1, 1])
        while n > 2:
            init.append(sum(init))
            init.popleft()
            n -= 1
        return init[n]