from sys import stdin

def kaing(M, N, x, y):
    while x <= M * N:
        if (x - y) % N == 0:
            return x
        x += M
    return -1

for _ in range(int(stdin.readline())):
    print(kaing(*map(int, stdin.readline().rstrip().split())))