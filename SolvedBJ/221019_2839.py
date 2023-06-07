N = int(input())
if N == 4:
    answer = -1
elif N == 3:
    answer = 1
elif N == 7:
    answer = -1
else:

    five, rem = divmod(N, 5)
    if rem == 0:
        answer = five
    elif rem == 1:
        answer = five + 1  # (five - 1) + 2
    elif rem == 2:
        answer = five + 2  # (five - 2) + 4
    elif rem == 3:
        answer = five + 1
    elif rem == 4:
        answer = five + 2  # 1 + (five - 1) + 2

print(answer)