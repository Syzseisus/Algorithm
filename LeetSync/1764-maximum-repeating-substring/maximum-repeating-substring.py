class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        m = len(sequence)
        n = len(word)
        avail = m // n
        k = 0
        for i in range(avail + 1):
            repeat = word * i
            if repeat in sequence:
                k = i
        
        return k