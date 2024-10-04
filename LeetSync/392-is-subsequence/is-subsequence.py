class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # 예외 1: s가 공백인 경우
        if not s:
            return True
        # 예외 2: s가 더 길 경우
        if len(s) > len(t):
            return False
        # 예외 3: 길이가 1일 경우
        if len(s) == len(t) == 1:
            return s == t

        ind = 0
        for mother in t:
            # print(ind, s, mother, end='')
            if mother == s[ind]:
                ind += 1
                # print("YES!")
            # else:
                # print()
            if ind == len(s):
                return True
        
        return ind == len(s)