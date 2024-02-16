class Solution:
    def decodeString(self, s):
        # s에 있는 문자들 stack으로 쌓음
        stack = []
        for c in s:
            # ]가 나올 때까지 다 넣음
            if c != ']':
                stack.append(c)

            # ]가 나오면 [] 안을 그 앞에 만큼 반복
            # 뒤에서부터 확인하기 위해 stack 사용
            else:
                # [가 나올 때까지 string 갱신: 뒤로 넣어야됨
                string = ''
                while stack[-1] != '[':
                    string = stack.pop() + string
                stack.pop()     # [ 제거

                # 이제 숫자 찾기
                num = ''
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                num = int(num)

                # stack에 넣기
                stack.append(string * num)

        return ''.join(stack)          