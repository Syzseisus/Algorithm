'''Union Find
1. Union: 파티에 참석하는 사람들의 쌍에서
  - 사실을 아는 사람을 parent로 지정하고
    모르는 사람을 children으로 한다
  - 아는 사람끼리는 연결하지 않는다.
2. Find: 각 파티를 다시 돌면서
  - 참여하는 사람 중 parent가 있으면 진실을 얘기한다
'''

import sys

inp = lambda: sys.stdin.readline()

def find(x):
    # x의 parent 찾기
    if x != parent[x]:
        parent[x] = find(parent[x])
    
    return parent[x]

def union(a, b):
    # a와 b의 parent를 찾아서
    a = find(a)
    b = find(b)

    # 둘 다 사실을 알고 있다면 종료
    if (a in know_truth) and (b in know_truth):
        return
    
    # 한 명만 알고 있으면 parent update
    if a in know_truth:
        parent[b] = a
    elif b in know_truth:
        parent[a] = b
    else:
        # 둘 다 모르면 작은 애를 parent로 설정해둔다
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

N, M = map(int, inp().split())
know_truth = list(map(int, input().split()))[1:]

parties = []
parent = list(range(N + 1))

for _ in range(M):
    party_info = list(map(int, inp().split()))
    party_len = party_info[0]
    party = party_info[1:]

    for i in range(party_len - 1):
        union(party[i], party[i + 1])
    
    parties.append(party)

answer = 0
for party in parties:
    for i in range(len(party)):
        if find(party[i]) in know_truth:
            break
    else:
        answer += 1
    
print(answer)