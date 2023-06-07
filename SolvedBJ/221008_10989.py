import sys

input = lambda: sys.stdin.readline()

count = [0 for _ in range(100001)]
for _ in range(int(input())):
    count[int(input())] += 1

for n in range(100001):
    for cnt in range(count[n]):
        sys.stdout.write("%d\n" %n)