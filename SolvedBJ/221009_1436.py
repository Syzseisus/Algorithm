import sys

N = int(sys.stdin.readline())
count = 0

for i in range(6660000):
    if '666' in str(i):
        count += 1
    
    if count == N:
        break

print(i)