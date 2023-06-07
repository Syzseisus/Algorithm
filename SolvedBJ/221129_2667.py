from sys import stdin

N = int(stdin.readline())

houses = [[i for i in stdin.readline().rstrip()] for _ in range(N)]

count = []
def bfs(y, x):
    if not (0 <= y < N and 0 <= x < N):
        return False

    if houses[y][x] == '1':
        count.append(1)
        houses[y][x] = '0'

        bfs(y - 1, x)
        bfs(y + 1, x)
        bfs(y, x - 1)
        bfs(y, x + 1)

        return True

    return False


answer = 0
answer_list = []
for y in range(N):
    for x in range(N):
        ind = x * N + y
        if bfs(y, x):
            answer += 1
            answer_list.append(len(count))
            count = []

answer_list.sort()
print(answer, *answer_list, sep='\n')