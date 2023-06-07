N, X = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))

print(*list(i for i in arr if i < X))