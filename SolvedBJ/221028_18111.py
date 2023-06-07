'''깎은 걸로 메우기 가능
맞출 수 있는 높이는
가장 낮은 높이(min_)부터
(sum(land - min_) + inven) // landsize 까지
'''

from sys import stdin

inp = lambda: stdin.readline().rstrip().split()
N, M, B = map(int, inp())
land = [list(map(int, inp())) for _ in range(N)]
# print(land)
min_ = min(map(min, land))
land_size = N * M
tot_block = sum(map(sum, land)) - land_size * min_ + B
max_ = (tot_block // land_size) + min_

# print(min_, max_)

# 최대 소요시간은 모든 블럭을 제거하고 다시 쌓는 시간
ans_time = 3 * land_size * 300
ans_height = 0
for h in range(min_, max_ + 1):
    time = 0
    for i in range(N):
        for j in range(M):
            if land[i][j] > h:
                time += 2 * (land[i][j] - h)
            else:
                time += h - land[i][j]
    if ans_time >= time:
        ans_time = time
        ans_height = h
    # print(h, ans_time, ans_height)
        
print(ans_time, ans_height)