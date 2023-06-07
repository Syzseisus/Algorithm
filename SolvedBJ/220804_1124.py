import sys

A, B = map(int, sys.stdin.readline().split())

DP = [0] * (B + 1)
prime = [1] * 2 + [0] * (B - 1)
for i in range(2, B + 1):
    if not prime[i]:
        DP[i] = 1
        for j in range(2 * i, B + 1, i):
            prime[j] = 1

for i in range(B + 1):
    if not DP[i]:
        for j in range(2, B + 1):
            if not (i % j):
                DP[i] = DP[i // j] + 1
                break

answer = 0
for i in range(A, B + 1):
    if not prime[DP[i]]:
        answer += 1

print(answer)
