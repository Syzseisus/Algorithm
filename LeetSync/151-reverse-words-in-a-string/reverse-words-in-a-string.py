from collections import deque

class Solution:
    # 세 번 평균 
    def reverseWords(self, s: str) -> str:
        # deque로 word 하나씩 stack 쌓기
        words = deque([])
        word = ''
        for char in s:
            # char가 공백이면
            if char == ' ':
                # word가 있을 경우 (공백이 여러 개 연속되는 경우를 skip하기 위함)
                if word != '':
                    # word를 stack하고 초기화
                    words.appendleft(word)
                    word = ''
                continue
            # char가 공백이 아니면 word 계속 늘리기
            word += char

        # for문 끝났는데 word가 남아 있으면 걔도 stack 하기
        if word != '':
            words.appendleft(word)
        
        # join해서 정답 words 생성
        return ' '.join(words)
            