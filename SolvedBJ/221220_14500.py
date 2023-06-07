from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())
array = [list(map(int, stdin.readline().split())) for _ in range(N)]


def tetris_Long():
    ans = 0
    # horizontal
    for r in range(N):
        for c in range(M - 3):
            sum_ = 0
            for k in range(c, c + 4):
                sum_ += array[r][k]
            ans = max(ans, sum_)

    # vertical
    for r in range(N - 3):
        for c in range(M):
            sum_ = 0
            for k in range(r, r + 4):
                sum_ += array[k][c]
            ans = max(ans, sum_)

    return ans


def tetris_Bent():
    ans = 0
    for r in range(N - 2):
        for c in range(M - 2):
            # 3- + 1|
            # down
            sum_d_h = array[r][c] + array[r][c+1] + array[r][c+2]
            sum_d_1 = sum_d_h + array[r+1][c]
            sum_d_2 = sum_d_h + array[r+1][c+1]
            sum_d_3 = sum_d_h + array[r+1][c+2]
            sum_d_N = array[r][c] + array[r][c+1] + array[r+1][c+1] + array[r+1][c+2]
            # up
            sum_u_h = array[r+1][c] + array[r+1][c+1] + array[r+1][c+2]
            sum_u_1 = sum_u_h + array[r][c]
            sum_u_2 = sum_u_h + array[r][c+1]
            sum_u_3 = sum_u_h + array[r][c+2]
            sum_u_N = array[r+1][c] + array[r+1][c+1] + array[r][c+1] + array[r][c+2]

            # 3| + 1-
            # right
            sum_r_v = array[r][c] + array[r+1][c] + array[r+2][c]
            sum_r_1 = sum_r_v + array[r][c+1]
            sum_r_2 = sum_r_v + array[r+1][c+1]
            sum_r_3 = sum_r_v + array[r+2][c+1]
            sum_r_N = array[r][c] + array[r+1][c] + array[r+1][c+1] + array[r+2][c+1]
            # left
            sum_l_v = array[r][c+1] + array[r+1][c+1] + array[r+2][c+1]
            sum_l_1 = sum_l_v + array[r][c]
            sum_l_2 = sum_l_v + array[r+1][c]
            sum_l_3 = sum_l_v + array[r+2][c]
            sum_l_N = array[r][c+1] + array[r+1][c+1] + array[r+1][c] + array[r+2][c]
            ans = max(ans, sum_r_1, sum_r_2, sum_r_3, sum_r_N, sum_l_1, sum_l_2, sum_l_3,
                      sum_l_N, sum_d_1, sum_d_2, sum_d_3, sum_d_N, sum_u_1, sum_u_2, sum_u_3, sum_u_N)

    # 3- + 1|
    # r == N-2
    for c in range(M - 2):
        # down
        sum_d_h = array[N-2][c] + array[N-2][c+1] + array[N-2][c+2]
        sum_d_1 = sum_d_h + array[N-1][c]
        sum_d_2 = sum_d_h + array[N-1][c+1]
        sum_d_3 = sum_d_h + array[N-1][c+2]
        sum_d_N = array[N-2][c] + array[N-2][c+1] + array[N-1][c+1] + array[N-1][c+2]
        # up
        sum_u_h = array[N-1][c] + array[N-1][c+1] + array[N-1][c+2]
        sum_u_1 = sum_u_h + array[N-2][c]
        sum_u_2 = sum_u_h + array[N-2][c+1]
        sum_u_3 = sum_u_h + array[N-2][c+2]
        sum_u_N = array[N-1][c] + array[N-1][c+1] + array[N-2][c+1] + array[N-2][c+2]
        ans = max(ans, sum_d_1, sum_d_2, sum_d_3, sum_d_N, sum_u_1, sum_u_2, sum_u_3, sum_u_N)

    # 3| + 1-
    # c == M-2
    for r in range(N - 2):
        # right
        sum_r_v = array[r][M-2] + array[r+1][M-2] + array[r+2][M-2]
        sum_r_1 = sum_r_v + array[r][M-1]
        sum_r_2 = sum_r_v + array[r+1][M-1]
        sum_r_3 = sum_r_v + array[r+2][M-1]
        sum_r_N = array[r][M-2] + array[r+1][M-2] + array[r+1][M-1] + array[r+2][M-1]
        # left
        sum_l_v = array[r][M-1] + array[r+1][M-1] + array[r+2][M-1]
        sum_l_1 = sum_l_v + array[r][M-2]
        sum_l_2 = sum_l_v + array[r+1][M-2]
        sum_l_3 = sum_l_v + array[r+2][M-2]
        sum_l_N = array[r][M-1] + array[r+1][M-1] + array[r+1][M-2] + array[r+2][M-2]
        ans = max(ans, sum_r_1, sum_r_2, sum_r_3, sum_r_N, sum_l_1, sum_l_2, sum_l_3, sum_l_N)

    return ans


def tetris_square():
    ans = 0
    for r in range(N-1):
        for c in range(M-1):
            sum_ = array[r][c] + array[r+1][c] + array[r][c+1] + array[r+1][c+1]
            ans = max(ans, sum_)

    return ans


print(max(tetris_Long(), tetris_Bent(), tetris_square()))
