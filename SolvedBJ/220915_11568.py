'''
LIS (Longes Increasing Sequence), DP 문제
'''

import sys
from bisect import bisect_left as bl

inp = lambda: sys.stdin.readline()

# N = int(inp())
# cards = list(map(int, inp().rstrip().split()))

def main(N, cards):
    DP = [1] * N
    for e in range(1, N):
        for s in range(e):
            if (cards[s] < cards[e]) and (DP[e] < DP[s] + 1):
                DP[e] = DP[s] + 1

    print(max(DP))


def BS(N, cards):
    DP = [cards[0]]
    for c in cards:
        if c > DP[-1]:
            DP.append(c)
        else:
            DP[bl(DP, c)] = c
    
    print(len(DP))
            


if __name__ == '__main__':
    N = [5, 8, 1, 2, 2, 5, 9]
    cards = [[8, 9, 1, 2, 10],
             [5, 4, 3, 2, 1, 6, 7, 8],
             [1],
             [1, 1],
             [2, 1],
             [1, 2, 10, 3, 4],
             [5, 4, 3, 1, 6, 7, 2, 8, 9]]
    output = [3, 4, 1, 1, 1, 4, 5]
    for i in range(len(N)):
        main(N[i], cards[i])
        BS(N[i], cards[i])
        print(f"answer: {output[i]}")