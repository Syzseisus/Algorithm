# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         """
#         Do not return anything, modify s in-place instead.
#         """
#         n = len(s)
        
#         for i in range(n//2):
#             s[i], s[n-i-1] = s[n-i-1], s[i]
        
#         return s
    
    
class Solution:
    def reverseString(self, s):
        l = 0
        r = len(s) - 1
        
        def reverse(l, r, s):
            if l >= r:
                return s
            else:
                s[l], s[r] = s[r], s[l]
                return reverse(l+1, r-1, s)
        
        return reverse(l, r, s)
            