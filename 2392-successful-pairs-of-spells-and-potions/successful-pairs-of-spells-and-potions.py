from bisect import bisect_right

class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        n = len(potions)
        potions.sort()
        answer = []
        for s in spells:
            tgt = (success - 1) // s
            ind = bisect_right(potions, tgt)
            answer.append(n - ind)
        
        return answer

