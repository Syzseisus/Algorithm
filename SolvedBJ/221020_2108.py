from sys import stdin

while True:
    N = int(stdin.readline())
    # N = 10000

    count = dict()
    sum_ = 0
    arr = []
    for _ in range(N):
        M = int(stdin.readline())
        count[M] = count.get(M, 0) + 1
        sum_ += M
        arr.append(M)
    # for _ in range(5001):
    #     M = 3999
    #     count[M] = count.get(M, 0) + 1
    #     sum_ += M
    #     arr.append(M)
    # for _ in range(4999):
    #     M = 4000
    #     count[M] = count.get(M, 0) + 1
    #     sum_ += M
    #     arr.append(M)

    arr.sort()
    count = sorted([(k, v) for k, v in count.items()], key=lambda x: (-x[1], x[0]))
    print()
    print(arr)
    print(count)

    print("avg", round(sum_ / N))

    print("mid", arr[N // 2])

    print("many", count[0][0] if len(count) == 1 or count[0][1] > count[1][1] else count[1][0])

    print("range", arr[-1] - arr[0])