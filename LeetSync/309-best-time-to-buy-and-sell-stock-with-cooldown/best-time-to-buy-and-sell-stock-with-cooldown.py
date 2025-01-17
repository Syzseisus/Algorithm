class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # 예외케이스
        if n == 1:
            return 0
        
        # DP 할당
        last_buy = [-10 ** 10 for _ in range(n)]
        last_sell = [0 for _ in range(n)]
        for i, p in enumerate(prices):
            last_sell[i] = max(last_sell[i - 1], p + last_buy[i - 1])
            last_buy[i] = max(last_buy[i - 1], last_sell[i - 2] - p)

        return last_sell[-1]
