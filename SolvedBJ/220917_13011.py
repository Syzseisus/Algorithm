import sys

inp = lambda: sys.stdin.readline()

N = int(inp())
C = list(map(int, inp().rstrip().split()))
W = list(map(int, inp().rstrip().split()))
rho = set([W[i] / C[i] for i in range(N)])

if len(rho) == 1:
    answer = 0.0

else:
    cand = []
    for r in rho:
        R = [abs(W[i] - (r * C[i])) for i in range(N)]
        cand.append(sum(R))
    answer = min(cand)

print(answer)