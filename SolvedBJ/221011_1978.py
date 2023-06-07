import sys

def is_prime(num):
    if num == 1:
        return 0
    if num == 2:
        return 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return 0
    else:
        return 1

_ = sys.stdin.readline()
numbers = list(map(int, sys.stdin.readline().rstrip().split()))

answer = 0
for num in numbers:
    answer += is_prime(num)

print(answer)