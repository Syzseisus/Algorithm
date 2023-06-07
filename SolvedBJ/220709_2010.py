import sys

N = int(sys.stdin.readline())

answer = 1
for _ in range(N):
    answer -= 1
    multi = int(sys.stdin.readline())
    answer += multi

print(answer)
