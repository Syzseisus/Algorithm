import sys
import heapq as hq

inp = lambda: sys.stdin.readline()

N = int(inp())
dasom = -int(inp())

if N == 1:
    print(0)

else:
    competitor = []
    for _ in range(N - 1):
        n_people = -int(inp())
        hq.heappush(competitor, n_people)

    bribe = 0
    while competitor[0] <= dasom:
        strongest = hq.heappop(competitor)
        bribe += 1
        dasom -= 1
        hq.heappush(competitor, strongest + 1)
    
    print(bribe)