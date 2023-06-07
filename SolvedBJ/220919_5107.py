# check: x와 그의 ind가 같은지 확인
# 같지 않다면 계속 돌면서 x를 업데이트

import sys
from collections import defaultdict

inp = lambda: sys.stdin.readline()

def pcd(arr):
    ans = []
    for name in names:
        if not check[name]:
            tgt = names[name]
            temp = [name]
            check[tgt] = True

            while name != tgt:
                temp.append(tgt)
                check[tgt] = True
                tgt = names[tgt]
            ans.append(temp)
    print(ans)
    return len(ans)

T = 1
while True:
    N = int(inp())
    if N == 0:
        break

    names = dict()
    check = defaultdict(bool)
    for _ in range(N):
        person = inp().rstrip().split()
        names[person[0]] = person[1]
        for p in person:
            check[p] = False
    print(names)
    
    print(f"{T} {pcd(names)}")
    T += 1