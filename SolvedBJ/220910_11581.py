import sys

inp = lambda: sys.stdin.readline()
INF = float('inf')

def help():
    for src in range(N):
        for tgt in range(N):
            # 1번에서 갈 수 있는 cycle만 가능
            if 0 < graph[0][tgt] < INF:
                if (0 < graph[src][tgt] < INF) and (0 < graph[tgt][src] < INF):
                    return "CYCLE"
    
    return "NO CYCLE"

    
N = int(inp())

graph = [[INF] * N for _ in range(N)]
for i in range(N - 1):
    M = int(inp())
    temp = list(map(int, inp().strip().split()))
    
    for j in range(M):
        graph[i][temp[j] - 1] = 1


for mid in range(N):
    for src in range(N):
        for tgt in range(N):
            graph[src][tgt] = min(
                graph[src][tgt], graph[src][mid] + graph[mid][tgt]
            )

print(f"{help()}")