from sys import stdin

N, M = map(int, stdin.readline().rstrip().split())
arr = list(map(int, stdin.readline().rstrip().split()))
arr.sort()

low = 1
high = arr[-1]
while low <= high:
    mid = (low + high) // 2
    get_ = 0
    for i in arr:
        if i > mid:
            get_ += (i - mid)
    if get_ >= M:
        low = mid + 1
    else:
        high = mid - 1
        
print(high)
