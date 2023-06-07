import sys

read = lambda: sys.stdin.readline()

N = int(read())

friend = [list(read().strip()) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]

for first in range(N):
    for me in range(N):
        for second in range(N):
            if me == second:
                continue

            second_to_me = friend[me][second] == "Y"
            first_to_me = friend[me][first] == "Y"
            second_to_first = friend[first][second] == "Y"
            if second_to_me or (first_to_me and second_to_first):
                visited[me][second] = 1

answer = 0
for i in visited:
    answer = max(answer, sum(i))
print(answer)
