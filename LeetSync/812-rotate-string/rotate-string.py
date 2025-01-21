class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        cnt = 0
        while cnt < n:
            s = s[1:] + s[0]
            if s == goal:
                return True
            cnt += 1
        return False