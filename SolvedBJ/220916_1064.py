import sys

def line(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

xa, ya, xb, yb, xc, yc = map(int, sys.stdin.readline().rstrip().split())
A = (xa, ya)
B = (xb, yb)
C = (xc, yc)

# 불가능: 한 직선 상에 있을 때
if round(((yb - ya) * (xc - xb)), 9) == round(((yc - yb) * (xb - xa)), 9):
    answer = -1.0

# 가능: ABCD, ACBD, ABDC
else:
    ABCD = 2 * (line(A, B) + line(B, C))
    ACBD = 2 * (line(A, C) + line(B, C))
    ABDC = 2 * (line(A, B) + line(A, C))
    max_ = max(ABCD, ACBD, ABDC)
    min_ = min(ABCD, ACBD, ABDC)
    
    answer = abs(max_ - min_)

print(answer)