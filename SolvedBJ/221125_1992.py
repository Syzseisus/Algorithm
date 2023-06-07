from sys import stdin


N = int(stdin.readline())
img = [[i for i in stdin.readline().rstrip()] for _ in range(N)]


def compress(x, y, size):
    global N
    pixel = img[x][y]
    flag = 0
    for i in range(x, x+size):
        for j in range(y, y+size):
            # 다른 게 나오면 잘라서 진행
            if (pixel != img[i][j]):
                print('(', end='')
                compress(x, y, size//2)
                compress(x, y+size//2, size//2)
                compress(x+size//2, y, size//2)
                compress(x+size//2, y+size//2, size//2)
                print(')', end='')
                flag = 1
                return

    if flag and N != 1 and size == N:
        print('(', end='')

    print(pixel, end='')

    if flag and N != 1 and size == N:
        print(')')


compress(0, 0, N)
