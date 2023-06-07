'''분할 정복
 0  1 |  4  5
 2  3 |  6  7
------|-------
 8  9 | 12 | 13
       ----|----
10 11 | 14 | 15

13을 찾고자한다. (N = 2r = 2, c = 3)
네 분할 = 사분면 활용

1. 4사분면이니까 사분면(N * N)을 세 개 지난 상태이다
    -> answer = 3 * N * N
2. 이제 4사분면 안으로 들어 왔다.
    -> r = 0, c = 1
3. 여기서는 2사분면에 있다
    -> answer = 3 * N * N + 1 * N * N
'''

import sys

N, r, c = map(int, sys.stdin.readline().split())

answer = 0
while N > 0:
    N -= 1
    border = 2 ** N

    # 제1사분면
    if r < border and c < border:
        answer += border * border * 0
    # 제2사분면
    elif r < border and c >= border:
        answer += border * border * 1
        c -= border
    # 제3사분면
    elif r >= border and c < border:
        answer += border * border * 2
        r -= border
    # 제4사분면
    elif r >= border and c >= border:
        answer += border * border * 3
        r -= border
        c -= border

print(answer)