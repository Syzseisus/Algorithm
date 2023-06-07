import sys

ans_max = int(sys.stdin.readline())
ans_ind = 1
for i in range(2, 10):
    N = int(sys.stdin.readline())
    if ans_max < N:
        ans_max = N
        ans_ind = i

print(ans_max)
print(ans_ind)
