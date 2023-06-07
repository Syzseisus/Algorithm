import sys

inp = lambda: map(int, sys.stdin.readline().strip().split(':'))

c_h, c_m, c_s = inp()
t_h, t_m, t_s = inp()

# 최소 1초 최대 24시간 -> 똑같으면 24시간 기다림
if t_h == c_h and t_m == c_m and t_s == c_s:
    w_h = 24
    w_m = 0
    w_s = 0

else:
    if t_s < c_s:
        t_m -= 1
        t_s += 60

    if t_m < c_m:
        t_h -= 1
        t_m += 60

    if t_h < c_h:
        t_h += 24

    w_h = t_h - c_h
    w_m = t_m - c_m
    w_s = t_s - c_s

print(f"{w_h:02}:{w_m:02}:{w_s:02}")