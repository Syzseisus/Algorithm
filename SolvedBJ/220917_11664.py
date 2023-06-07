import sys

def dist(A, B):
    return sum([pow((A[i] - B[i]), 2) for i in range(3)]) ** 0.5

Ax, Ay, Az, Bx, By, Bz, Cx, Cy, Cz = map(int, sys.stdin.readline().rstrip().split())

A = [Ax, Ay, Az]
B = [Bx, By, Bz]
C = [Cx, Cy, Cz]
d = [Bx - Ax, By - Ay, Bz - Az]

l = 0
r = 1
while (r - l) >= 1e-12:
    p = (2 * l + r) / 3
    q = (l + 2 * r) / 3
    
    P = [A[i] + d[i] * p for i in range(3)]
    Q = [A[i] + d[i] * q for i in range(3)]
    
    dP = dist(P, C)
    dQ = dist(Q, C)

    if dP > dQ:
        l = p
    else:
        r = q

final = (l + r) / 2
F = [A[i] + d[i] * final for i in range(3)]
print(dist(F, C))