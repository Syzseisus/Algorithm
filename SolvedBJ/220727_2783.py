import sys

X, Y = map(int, sys.stdin.readline().split())
answer = X / Y

N = int(sys.stdin.readline())
for i in range(N):
    X, Y = map(int, sys.stdin.readline().split())
    answer = min(answer, X / Y)

print(f"{answer * 1000:.2f}")
