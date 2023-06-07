import sys

inp = lambda: sys.stdin.readline()
INF = int(1e9)

N = int(inp())
graph = [list(map(int, inp().strip().split())) for _ in range(N)]

# DP * bitmask
# DP[i][j] -> i: current / j: bitmask, visited
# DP[0][0011(2)]: 현재 0번 / 0,1 방문:  1 -> "0 -> (2", 3)
# DP[2][0111(2)]: 현재 2번 / 0,1,2 방문:(0, 1) -> 2 -> 3
# 따라서 DP[0][0011] = DP[2][0111] + graph[0][2]
#                                   == ""에 해당하는 부분
# 근데 타임아웃 -> 뒤집어야됨
# DP[2][0111] = DP[0][0011] + graph[0][2]와 같은 식.

# bitmask
# 1. 1 << next(i)하면
#    i가 0 ~ 3이라 0000 중에 next만 1로 만들 수 있음.
# 2. visited | (1 << next(i))하면
#    visited에다가 |를 통해 next를 1로 변경할 수 있음.

DP = [[0] * (1 << (N - 1)) for _ in range(N)]
# print(DP)

def dfs(x, visited):
    # 기록된 memo 참고
    if DP[x][visited] != 0:
        return DP[x][visited]
    
    # 모든 도시 방문 완료
    if visited == (1 << (N - 1)) - 1:
        if graph[x][0]:
            return graph[x][0]
        else:
            return INF

    min_route = INF
    # 모든 도시에 대해
    for i in range(1, N):
        # 경로 없거나 방문했으면 skip
        if not graph[x][i] or visited & (1 << (i - 1)):
            continue
        
        next_visit = visited | (1 << (i - 1))
        next_dist = graph[x][i] + dfs(i, next_visit)
        if min_route > next_dist:
            min_route = next_dist

    DP[x][visited] = min_route
    return min_route

print(dfs(0, 0))