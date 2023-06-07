import sys

P, K = map(int, sys.stdin.readline().split())

flag = 0
for i in range(2, K):
    if P % i == 0:
        flag = 1
        break
if flag:
    print(f"BAD {i}")
else:
    print("GOOD")
