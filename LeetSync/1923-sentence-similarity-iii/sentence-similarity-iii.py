'''
가능한 케이스
A B C / A C
A B / A
A B / B
'''


class Solution:
    def areSentencesSimilar(self, st1: str, st2: str) -> bool:
        # word 리스트로 변경
        st1 = st1.split(" ")
        st2 = st2.split(" ")

        len1 = len(st1)
        len2 = len(st2)
        
        # 짧은 걸 1로 설정
        if len1 > len2:
            st1, st2 = st2[:], st1[:]
            len1, len2 = len2, len1
        elif len1 == len2:
            return st1 == st2
        
        i = 0
        # 왼쪽부터 탐색
        while i < len1 and st1[i] == st2[i]:
            i += 1
        # 오른쪽부터 탐색
        while i < len1 and st1[i] == st2[len2 - len1 + i]:
            i += 1

        return i == len1