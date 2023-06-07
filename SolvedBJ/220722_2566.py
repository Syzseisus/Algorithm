import sys

ans_max = -1
ans_row = 0
ans_col = 0

for row in range(1, 10):
    data = list(map(int, sys.stdin.readline().split()))
    temp_max = max(data)
    if ans_max < temp_max:
        ans_max = temp_max
        ans_row = row
        ans_col = data.index(temp_max)

print(ans_max)
print(ans_row, ans_col + 1)
