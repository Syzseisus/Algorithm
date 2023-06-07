from sys import stdin
M, N = map(int, stdin.readline().rstrip().split())

for i in range(M, N + 1):
    if i == 1:
        continue
    elif i == 2:
        print(i)
    else:
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            print(i)
