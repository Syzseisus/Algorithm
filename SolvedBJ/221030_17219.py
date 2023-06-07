from sys import stdin

N, M = map(int, stdin.readline().split())
pwdict = {}
for _ in range(N):
    url, pw = stdin.readline().split()
    pwdict[url] = pw

for _ in range(M):
    print(pwdict[stdin.readline().rstrip()])