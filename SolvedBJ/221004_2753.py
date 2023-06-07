N = int(input())
answer = 1 if (N % 4 == 0 and N % 100 != 0) or (N % 400 == 0) else 0
print(answer)