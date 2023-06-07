import sys
from collections import defaultdict, deque

inp = lambda: sys.stdin.readline()

def DFS(node):
    visited = [False] * (N + 1)
    cnt = 1
    visited[node] = True
    q = deque([node])
    while q:
        src = q.popleft()
        for tgt in trust[src]:
            if not visited[tgt]:
                q.append(tgt)
                visited[tgt] = True
                cnt += 1
    
    return cnt

N, M = map(int, inp().split())

trust = defaultdict(set)
for _ in range(M):
    src, tgt = map(int, inp().split())
    trust[tgt].add(src)

counts = []
max_cnt = 0
for node in range(1, N + 1):
    cnt = DFS(node)
    max_cnt = max(cnt, max_cnt)
    counts.append([node, cnt])

for i, cnt in counts:
    if cnt == max_cnt:
        print(i, end=' ')