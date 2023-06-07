N, M = map(int, input().split())
cards = list(map(int, input().split()))

def bljack():
    max_ = 0
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                sum_ = cards[i] + cards[j] + cards[k]
                if sum_ > M:
                    continue
                elif sum_ == M:
                    print(M)
                    return
                else:
                    max_ = max(max_, sum_)

    print(max_)

bljack()