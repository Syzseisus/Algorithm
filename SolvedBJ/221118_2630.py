from math import log
from sys import stdin

N = int(stdin.readline())
paper = [list(map(int, stdin.readline().rstrip().split())) for _ in range(N)]
answer = [[0, 0] for _ in range(8)]

def helper(paper, N):
    index = round(log(N, 2))
    if N == 1:
        answer[index][paper[0][0] + 1] += 1
    elif N == 2:
        temp1 = sum(p.count(0) for p in paper)
        temp2 = 4 - temp1

        if temp1 == 4:
            answer[index][0] += 1
        elif temp2 == 4:
            answer[index][1] += 1
        else:
            answer[index][0] += temp1
            answer[index][1] += temp2

    else:
        for i in range(4):
            cut = []
            for j in range(N // 2):
                cut.append(paper[(i//2) * (N//2) + j][(i%2) * (N//2):(i%2) * (N//2) + N//2])
            helper(cut, N//2)

        if (answer[index-1][0] == 4 and
            answer[index-1][1] == 0):
            answer[index][0] += 1
            answer[index-1][0] = 0
        elif (answer[index-1][0] == 0 and
              answer[index-1][1] == 4):
              answer[index][1] += 1
              answer[index-1][1] = 0
        else:
            answer[index][0] += answer[index-1][0]
            answer[index][1] += answer[index-1][1]
            answer[index-1] = [0, 0]


index = round(log(N, 2))
helper(paper, N)
print(*answer[index], sep='\n')