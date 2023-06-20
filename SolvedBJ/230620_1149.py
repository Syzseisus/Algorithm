import sys

N = int(sys.stdin.readline())
cost = []
for _ in range(N):
    cost.append(list(map(int, sys.stdin.readline().split())))


def sol(N, cost):
    DP = [[0 for _ in range(3)] for _ in range(N)]
    DP[0] = cost[0]
    for h in range(1, N):
        for p in range(3):
            mini = 1000 * 1000  # 최대 1000개의 집, 비용 최대 1000
            for n in range(3):
                if p == n:
                    continue
                mini = min(mini, DP[h - 1][n])
                DP[h][p] = mini + cost[h][p]

    return min(DP[-1])


print(sol(N, cost))


# region: for test
# Ns = [3, 3, 3, 6, 8]
# costs = [
#     [[26, 40, 83], [49, 60, 57], [13, 89, 99]],
#     [[1, 100, 100], [100, 1, 100], [100, 100, 1]],
#     [[1, 100, 100], [100, 100, 100], [1, 100, 100]],
#     [[30, 19, 5], [64, 77, 64], [15, 19, 97], [4, 71, 57], [90, 86, 84], [93, 32, 91]],
#     [
#         [71, 39, 44],
#         [32, 83, 55],
#         [51, 37, 63],
#         [89, 29, 100],
#         [83, 58, 11],
#         [65, 13, 15],
#         [47, 25, 29],
#         [60, 66, 19],
#     ],
# ]
# answers = [96, 3, 102, 208, 253]

# correct = 0
# for i, N in enumerate(Ns):
#     cost = costs[i]
#     answer = answers[i]
#     resp = sol(N, cost)
#     if answer == resp:
#         correct += 1
#         print("correct.")
#     else:
#         print(f"  wrong. my: {resp}, answer: {answer}")

# print("score:", correct / len(Ns) * 100)
# endregion
