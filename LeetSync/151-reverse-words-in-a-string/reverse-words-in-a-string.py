from collections import deque

class Solution:
    # def reverseWords(self, s: str) -> str:
    #     # s.split() -> words를 word로 찢음
    #     # [::-1] -> 순서 뒤집음
    #     # ' '.join() -> word를 words로 합침
    #     return ' '.join(s.split()[::-1])
    def reverseWords(self, s: str) -> str:
        words = deque([])
        word = ''
        for char in s:
            if char == ' ':
                if word != '':
                    words.appendleft(word)
                    word = ''
                continue
            word += char
        if word != '':
            words.appendleft(word)
        
        return ' '.join(words)
            