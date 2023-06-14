import sys

A, B = map(int, sys.stdin.readline().split())


def dfs(n, times):
    if n == B:
        return times
    elif n > B:
        return 40

    x = dfs(n * 2, times + 1)
    y = dfs(10 * n + 1, times + 1)

    return min(x, y)


answer = dfs(A, 1)
answer = -1 if answer == 40 else answer

print(answer)
