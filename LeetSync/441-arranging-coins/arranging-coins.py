# # k번째 row까지 코인을 채우려면 k(k+1)/2 개의 코인이 필요
# # k+1번째까지는 (k+1)(k+2)/2개의 코인이 필요
# # 따라서 k(k+1)/2 <= a < (k+1)(k+2)/2를 만족하는 k가 답
# # 풀어보면
# # (-3+sqrt(1+8a))/2 < a <= (-1+sqrt(1+8a))/2 가 나오고
# # 좌변과 우변은 1차이이므로
# # a = floor(우변) = [우변] (가우스기호)


# from math import sqrt # 필요한 루트만 import해서 메모리 down

# class Solution:
#     def arrangeCoins(self, n):
#         return floor((-1+sqrt(1+8*n))/2)
    
    
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