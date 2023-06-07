from sys import stdin

arr = []
for _ in range(int(stdin.readline())):
    N = int(stdin.readline())
    if N == 0 and arr:
        arr.pop()
    else:
        arr.append(N)

print(sum(arr))
