T = int(input())

for _ in range(T):
    R, S = input().strip().split()
    R = int(R)

    print(''.join(i * R for i in S))
