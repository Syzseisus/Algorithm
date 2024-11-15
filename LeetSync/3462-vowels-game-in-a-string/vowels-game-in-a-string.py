from collections import Counter

class Solution:
    def doesAliceWin(self, s: str) -> bool:
        # vowel 개수 세기
        counter = Counter(s)
        num_vowels = sum(counter[k] for k in 'aeiou')
        if num_vowels == 0:
            return False

#         # 홀수면 Alice가 다 가져가서 이기고,
#         # 4 이상의 짝수면 
#         if counter % 2:
#             return True
        return True
        