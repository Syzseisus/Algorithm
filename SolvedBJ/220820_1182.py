import sys

inp = lambda: sys.stdin.readline()

N, S = map(int, inp().split())
array = list(map(int, inp().split()))

answer = [0]

def sub_sum(ind, sum_):
    if ind >= N:
        return
    
    sum_ += array[ind]
    if sum_ == S:
        answer[0] += 1

    # ind를 택함
    sub_sum(ind + 1, sum_)
    # ind를 택하지 않음
    sub_sum(ind + 1, sum_ - array[ind])

sub_sum(0, 0)
print(answer[0])