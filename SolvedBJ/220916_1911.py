import sys
from tracemalloc import start

inp = lambda: sys.stdin.readline().rstrip().split()

N, L = map(int, inp())
pools = [tuple(map(int, inp())) for _ in range(N)]
pools.sort(key=lambda x: x[0])

curr_board = pools[0][0]
answer = 0
for s, e in pools:
    if e < curr_board:
        continue
    elif curr_board < s:
        curr_board = s

    uncovered = e - curr_board
    num_board, remain = divmod(uncovered, L)
    if remain:
        num_board += 1
    
    curr_board += num_board * L
    answer += num_board

print(answer)
