from sys import stdin
from collections import deque

for _ in range(int(stdin.readline())):
    A, B = map(int ,stdin.readline().split())
    
    q = deque()
    q.append((A, ''))
    visited = [False for _ in range(10000)]
    visited[A] = True
    while q:
        A, path = q.popleft()

        D = (2 * A) % 10000
        if D == B:
            print(path + 'D')
            break
        if not visited[D]:
            q.append((D, path + 'D'))
            visited[D] = True

        S = A - 1 if A else 9999
        if S == B:
            print(path + 'S')
            break
        if not visited[S]:
            q.append((S, path + 'S'))
            visited[S] = True

        L = (A % 1000) * 10 + (A // 1000)
        if L == B:
            print(path + 'L')
            break
        if not visited[L]:
            q.append((L, path + 'L'))
            visited[L] = True

        R = (A % 10) * 1000 + (A // 10)
        if R == B:
            print(path + 'R')
            break
        if not visited[R]:
            q.append((R, path + 'R'))
            visited[R] = True

# min_v = 10000
# min_a = set()
# max_v = 0
# max_a = set()
# for start in range(1, 10000, 2):
#     a = start
#     visited = set()
#     while a not in visited:
#         visited.add(a)
#         a = (a * 2) % 10000
    
#     if len(visited) > max_v:
#         max_v = len(visited)
#         max_a = set([start])
#     elif len(visited) == max_v:
#         max_a.add(start)
#     if len(visited) < min_v:
#         min_v = len(visited)
#         min_a = set([start])
#     elif len(visited) == min_v:
#         min_a.add(start)
    
# print(max_v, len(max_a))  # 504, 4000
# print(min_v, len(min_a))  # 5, 8 (625의 홀수 배)