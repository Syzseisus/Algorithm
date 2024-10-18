class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()

        answer = 0
        while s and g:
            if g[-1] <= s[-1]:
                g.pop()
                s.pop()
                answer += 1
            else:
                g.pop()
        
        return answer
        
                