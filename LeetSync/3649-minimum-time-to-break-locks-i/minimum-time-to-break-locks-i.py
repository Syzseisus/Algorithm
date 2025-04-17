class Solution:
    def findMinimumTime(self, strength: List[int], k: int) -> int:
        strength = tuple(sorted(strength, reverse=True))

        @lru_cache
        def dp(state, x):
            if len(state) == 0:
                return 0
            
            answer = float('inf')
            for i, s in enumerate(state):
                time = (s + x - 1) // x
                new_state = state[:i] + state[i + 1:]
                curr = time + dp(new_state, x + k)
                answer = min(answer, curr)
            
            return answer
        
        return dp(strength, 1)