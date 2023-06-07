import sys

num_div = int(sys.stdin.readline())
dividors = list(map(int, sys.stdin.readline().strip().split()))

if num_div == 1:
    answer = dividors[0] ** 2
else:
    dividors.sort()
    answer = dividors[0] * dividors[-1]

print(answer)