from sys import stdin

def move(N, K):
    if N >= K:
        return N - K
    elif K == 1:
        return 1
    elif K % 2:
        return min(move(N, K + 1), move(N, K - 1)) + 1
    else:
        return min(K - N, move(N, K // 2) + 1)

print(move(*map(int, stdin.readline().split())))