class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        days_range = range(days[-1] + 1)
        dp = [0 for _ in days_range]
        days = set(days)
        
        for i in days_range:
            if i not in days:
                dp[i] = dp[i - 1]
            else:
                one_day = dp[max(0, i - 1)] + costs[0]
                weekly = dp[max(0, i - 7)] + costs[1]
                monthly = dp[max(0, i - 30)] + costs[2]
                dp[i] = min(one_day, weekly, monthly)
        
        return dp[-1]