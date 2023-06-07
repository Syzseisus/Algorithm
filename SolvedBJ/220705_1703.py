import sys
import time

while True:
    data = list(map(int, sys.stdin.readline().split()))
    if len(data) == 1:
        break

    branches = 1
    for i in range(1, len(data), 2):
        branches *= data[i]
        branches -= data[i + 1]
    print(branches)
