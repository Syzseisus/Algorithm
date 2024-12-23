class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        n = len(skills)
        k = min(k, n - 1)
        win = 0
        i = 0
        for j in range(1, n):
            if skills[i] < skills[j]:
                i = j
                win = 1
            else:
                win += 1
            if win == k:
                break
        return i
