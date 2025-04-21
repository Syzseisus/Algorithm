from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_cnt = Counter(s)
        t_cnt = Counter(t)

        return next((t_cnt - s_cnt).elements())