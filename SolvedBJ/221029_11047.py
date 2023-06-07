from sys import stdin

N, K = map(int, stdin.readline().split())
coins = [int(stdin.readline()) for _ in range(N)]
coins.sort(reverse=True)

answer = 0
for c in coins:
    if c <= K:
        d, K = divmod(K, c)
        answer += d
    if K == 0:
        break
print(answer)
