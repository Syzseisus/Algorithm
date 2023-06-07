from sys import stdin

N = int(stdin.readline())
M = int(stdin.readline())
IOI = stdin.readline().rstrip()

answer = 0
cnt = 0     # 누적 최소 단위 개수
i = 0
while i < (M - 1):
    # i부터 시작해서 최소단위인 IOI가 있을 때를 탐색
    if IOI[i:i+3] == "IOI":
        # 두 칸(I부터 시작해야되니까) 건너감
        i += 2
        cnt += 1
        # 전체 도달하면
        if cnt == N:
            # 답 하나 추가하고 맨 앞의 최소단위 제거
            answer += 1
            cnt -= 1
    
    # 최소단위 만족 안하면 i+1부터 새로 시작
    else:
        i += 1
        cnt = 0
    
print(answer)