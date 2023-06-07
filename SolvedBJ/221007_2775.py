T = int(input())

DP = [[0 for _ in range(15)] for _ in range(15)]
DP[0] = [i for i in range(15)]

for r in range(1, 15):
    for c in range(15):
        DP[r][c] = sum(DP[r - 1][:c + 1])

# for i in range(14, -1, -1):
#     print(f"{i:2d}", DP[i])

for _ in range(T):
    print(DP[int(input())][int(input())])