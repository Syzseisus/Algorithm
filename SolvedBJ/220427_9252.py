import sys

sys.setrecursionlimit(100000)

str_1 = input()
str_2 = input()

L = [[0 for _ in range(len(str_2) + 1)] for _ in range(len(str_1) + 1)]  # 길이
S = [[0 for _ in range(len(str_2) + 1)] for _ in range(len(str_1) + 1)]  # 문자열


# update L ( O(N^2) )
for m in range(len(str_1) + 1):
    for n in range(len(str_2) + 1):
        # m = 0 or n = 0, base case
        if (m == 0) or (n == 0):
            L[m][n] = 0

        # str_1[m-1] == str_2[n-1]
        elif str_1[m - 1] == str_2[n - 1]:
            L[m][n] = L[m - 1][n - 1] + 1
            S[m][n] = 0

        # str_1[m-1] != str_2[n-1]
        else:
            left = L[m][n - 1]
            top = L[m - 1][n]
            if left > top:
                L[m][n] = left
                S[m][n] = 1
            else:
                L[m][n] = top
                S[m][n] = 2


# make string
def print_answer(m, n):
    # recurrsive end
    if (m == 0) or (n == 0):
        return None

    # 이때가 같은 문자 나올 때 (str_1[m-1] == str_2[n-1])
    if S[m][n] == 0:
        print_answer(m - 1, n - 1)
        print(str_1[m - 1], end="")

    # S[m][n] == 1: 왼쪽에서 왔음
    elif S[m][n] == 1:
        print_answer(m, n - 1)  # 그래서 n -= 1

    # S[m][n] == 2: 위에서 왔음
    elif S[m][n] == 2:
        print_answer(m - 1, n)  # 그래서 m -= 1


print(L[-1][-1])
if L[-1][-1]:
    print_answer(len(str_1), len(str_2))
