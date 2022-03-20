# Solved by Bineary Search

# params
# lb: Lower Bound
# ub: Upper Bound
# mid = (lb+ub)//2 : 중간값
# summ = 첫번째 줄에서 mid번째 줄까지 코인을 꽉 채웠을 때의 개수
# ** 1 + ... + n = n(n+1)/2

# 마지막에 있는 if 문:
# summ > n => 너무 많이 더했으니까 ub 줄임
# summ < n => 너무 저게 더했으니까 lb 늘임
# summ == n => 코인이 정확하게 staircase를 만드는 경우. -> return mid

# 처음에 있는 if 문:
# ub - lb == 1
# => lb줄 쌓으면 코인이 남고, ub줄 쌓으려면 코인이 부족한데 차이가 1이다
# => lb줄까지 complete row를 만들 수 있다. -> return lb

class Solution:
    def arrangeCoins(self, n):
        lb = 1
        ub = n
        while True:
            if ub - lb == 1: return lb

            mid = (lb+ub) // 2
            summ = mid*(mid+1) / 2
            if summ > n:
                ub = mid
            elif summ < n:
                lb = mid
            else:
                return mid

# Run time : 41ms
# Memory   : 13.8MB
