import sys

inp = lambda: sys.stdin.readline()

def integral(deg):
    return (pow(b, (deg + 1)) - pow(a, (deg + 1))) / (deg + 1)

def approx(eps):
    aprx = 0
    for deg, coeff in enumerate(C):
        deg = K - deg
        if coeff:
            temp = 0
            for k in range(N):
                temp += pow((a + k * dx + eps), deg)
            aprx += temp * coeff * dx
    
    return aprx


K = int(inp())
C = list(map(int, inp().strip().split()))
a, b, N = map(int, inp().strip().split())

# C = C[::-1]
dx = (b - a) / N

real = 0
for deg, coeff in enumerate(C):
    deg = K - deg
    real += integral(deg) * coeff

low = 0
high = dx
flag = False
while low <= high:
    eps = (low + high) / 2
    aprx = approx(eps)
    if abs(real - aprx) <= 1e-4:
        flag = True
        break
    elif real > aprx + 1e-4:
        low = eps
    elif aprx > real + 1e-4:
        high = eps

print(eps if flag else -1)