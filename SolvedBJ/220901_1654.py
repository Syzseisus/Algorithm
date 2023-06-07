import sys

inp = lambda: sys.stdin.readline()

K, N = map(int, inp().split())

wires = [int(inp()) for _ in range(K)]

left = 1
right = max(wires)

while left <= right:
    mid = (left + right) // 2
    target = sum([wire // mid for wire in wires])
    if target < N:
        right = mid - 1
    else:
        left = mid + 1

print(right)