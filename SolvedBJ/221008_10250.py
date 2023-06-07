for _ in range(int(input())):
    H, W, N = map(int, input().split())
    Y = N % H
    X = N // H
    if Y == 0:
        Y = H
    else:
        X = X + 1
    print(f"{Y}{X:02d}")