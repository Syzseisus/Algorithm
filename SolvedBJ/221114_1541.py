from sys import stdin

expr = stdin.readline().rstrip()

temp = ''
spl = []
for i in expr:
    if i.isdigit():
        temp += i
    else:
        spl.append(temp)
        spl.append(i)
        temp = ''
if temp:
    spl.append(temp)
# print(spl)


answer = 0

temp = 0
minus = False

for token in spl:
    if token == '-' or token == '+':
        if minus:
            answer -= temp
            temp = 0
        else:
            answer += temp
            temp = 0
    
    else:
        temp = int(token)
    
    if token == '-':
        minus = True

answer -= temp if minus else -temp

print(answer)