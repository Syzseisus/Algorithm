'''
a <= x <= b - 2
x: 삼각수
x+1: 제곱수
i번째 삼각수 = i * (i + 1) // 2
j번째 제곱수 = j ** 2
'''

import sys

inp = lambda: map(int, sys.stdin.readline().strip().split())

N = 1
while True:
    a, b = inp()
    if (a == 0) and (b == 0):
        break

    answer = 0

    t = 0
    while (t * (t + 1) // 2) < a:
        t += 1
    
    while (t * (t + 1) // 2) < (b - 1):
        s = (t * (t + 1) // 2) + 1
        if s ** 0.5 == int(s ** 0.5):
            answer += 1
        t += 1

    print(f"Case {N}: {answer}")
    N += 1
