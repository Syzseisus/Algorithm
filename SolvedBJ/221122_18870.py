'''
2   2  ->   2보다 작은 서로 다른 좌표   : -9, -10
4   3  ->   4보다 작은 서로 다른 좌표   : 2, -9, -10
-10 0  -> -10보다 작은 서로 다른 좌표   : X
4   3  ->   4보다 작은 서로 다른 좌표   : 2, -9, -10
-9  1  ->  -9보다 작은 서로 다른 좌표   : -10
'''

from sys import stdin

N = int(stdin.readline())
org = list(map(int, stdin.readline().rstrip().split()))
org_sort = sorted(set(org))
answer = {org_sort[i]: i for i in range(len(org_sort))}
print(*(answer[i] for i in org))