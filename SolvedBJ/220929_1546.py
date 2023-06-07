N = int(input())
arr = list(map(int, input().strip().split()))

print(((sum(arr) / N)) * (100 / max(arr)))