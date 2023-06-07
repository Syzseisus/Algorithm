word = input().strip().upper()

max_ = 0
flag = 0
answer = '?'
for alphabet in set(word):
    count = word.count(alphabet)
    if count == max_:
        flag = 1
    elif count > max_:
        flag = 0
        max_ = count
        answer = alphabet

answer = '?' if flag else answer
print(answer)