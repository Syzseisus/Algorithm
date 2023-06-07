# P(n) = P(n-1) + P(n-5)
# where P({1, 2, 3, 4, 5}) = {1, 1, 1, 2, 2}

from sys import stdin


DP = {
    1: 1, 2: 1, 3: 1, 4: 2, 5: 2
}
def pado(N):
    if N in DP:
        return DP[N]
    else:
        DP[N] = pado(N-1) + pado(N-5)
        return DP[N]


for _ in range(int(stdin.readline())):
    print(pado(int(stdin.readline())))