'''
1. 일단 (를 stack에 넣음
2. )가 왔다
    1) 직전이 )다: 새로운 쇠막대기 생성 -> answer += 1
    2) 직전이 (다: 새로운 레이저 생성 -> pop하고 answer += len(stack)
        stack에는 (들만 있는 상태이다. 이 (들은 훗날 쇠막대기가 될 애들이다.
        새로 생성된 레이저는 이 모두를 자르며 조각을 만들어낸다.
'''
inp = list(input())

answer = 0
stack = []
prev = ''
for i in inp:
    if i == "(":
        stack.append(i)
    
    else:
        if prev == "(":
            stack.pop()
            answer += len(stack)
        
        else:
            stack.pop()
            answer += 1
    prev = i

print(answer)