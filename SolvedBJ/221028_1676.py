N = int(input())

answer = N // 5
temp = answer
while temp >= 5:
    temp //= 5
    answer += temp

print(answer)