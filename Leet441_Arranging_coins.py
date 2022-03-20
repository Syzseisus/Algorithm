# Binary Search 사용하지 않은 알고리즘.


# k번째 row까지 코인을 채우려면 k(k+1)/2 개의 코인이 필요
# k+1번째까지는 (k+1)(k+2)/2개의 코인이 필요
# 따라서 k(k+1)/2 <= n < (k+1)(k+2)/2를 만족하는 k가 답
# 풀어보면
# (-3+sqrt(1+8n))/2 < k <= (-1+sqrt(1+8n))/2 가 나오고
# 좌변과 우변은 1차이이므로
# k = floor(우변) = [우변] (가우스기호)


from math import sqrt # 필요한 루트만 import해서 메모리 down

class Solution:
    def arrangeCoins(self, n):
        return floor((-1+sqrt(1+8*n))/2)
    
# Run time : 38ms
# Memory   : 13.9MB
