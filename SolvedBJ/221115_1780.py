'''
페이퍼에 대해서
전체 확인
안되면 -> 3으로 나눈 페이퍼 페이퍼로 진행
되면  -> 업데이트
'''

from math import log
from sys import stdin

N = int(stdin.readline())
paper = [list(map(int, stdin.readline().rstrip().split())) for _ in range(N)]
answer = [[0, 0, 0] for _ in range(9)]

def helper(paper, N):
    index = round(log(N, 3))
    if N == 1:
        answer[index][paper[0][0] + 1] += 1
    elif N == 3:
        temp1 = sum(p.count(-1) for p in paper)
        temp2 = sum(p.count(0) for p in paper)
        temp3 = 9 - temp1 - temp2

        if temp1 == 9:
            answer[index][0] += 1
        elif temp2 == 9:
            answer[index][1] += 1
        elif temp3 == 9:
            answer[index][2] += 1
        else:
            answer[index][0] += temp1
            answer[index][1] += temp2
            answer[index][2] += temp3

    else:
        for i in range(9):
            cut = []
            for j in range(N // 3):
                cut.append(paper[(i//3) * (N//3) + j][(i%3) * (N//3):(i%3) * (N//3) + N//3])
            helper(cut, N//3)

        if (answer[index-1][0] == 9 and
            answer[index-1][1] == 0 and
            answer[index-1][2] == 0):
            answer[index][0] += 1
            answer[index-1][0] = 0
        elif (answer[index-1][0] == 0 and
              answer[index-1][1] == 9 and
              answer[index-1][2] == 0):
              answer[index][1] += 1
              answer[index-1][1] = 0
        elif (answer[index-1][0] == 0 and
              answer[index-1][1] == 0 and
              answer[index-1][2] == 9):
              answer[index][2] += 1
              answer[index-1][2] = 0
        else:
            answer[index][0] += answer[index-1][0]
            answer[index][1] += answer[index-1][1]
            answer[index][2] += answer[index-1][2]
            answer[index-1] = [0, 0, 0]


index = round(log(N, 3))
helper(paper, N)
print(*answer[index], sep='\n')