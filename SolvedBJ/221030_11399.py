'''
값 = sum((N+1-i) * Pi)
그니까 Pi를 sort하면 됨
'''

from sys import stdin

N = int(stdin.readline())
P = list(map(int, stdin.readline().split()))
P.sort(reverse=True)
print(sum(P[i] * (i + 1) for i in range(N)))