import sys

n, m = map(int, sys.stdin.readline().split())

if n == m:
    answer = 1

else:
    # nCm == nC(n-m)
    # 정리하면 nCm = (n / 1) * (n - 1 / i) * ... * (n - m + 1 / n - m)
    answer = 1
    for i in range(1, min(m, n - m) + 1):
        answer *= n - i + 1
        answer //= i

print(answer)
