class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x == 0:
            return True

        row = str(x)
        col = row[::-1]
        
        return row == col