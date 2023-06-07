def GCD(a, b):
    if b == 0:
        return a
    
    return GCD(b, a % b)

A, B = map(int, input().split())
G = GCD(A, B)
L = A * B // G
print(G, L, sep='\n')
