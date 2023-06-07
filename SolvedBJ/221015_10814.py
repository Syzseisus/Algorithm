import sys
import heapq as hq

arr = []
for i in range(int(sys.stdin.readline())):
    age, name = sys.stdin.readline().rstrip().split()
    arr.append((int(age), name, i))

arr.sort(key=lambda x: (x[0], x[2]))

for age, name, _ in arr:
    print(age, name)