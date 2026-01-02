# DP Linear Time + Space
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        
        def dfs(i, buy):
            if i >= len(prices):
                return 0
            if (i, buy) in dp:
                return dp[(i, buy)]

            if buy:
                profit = dfs(i + 1, False) - prices[i]
                cooldown = dfs(i + 1, True)
                dp[(i, buy)] = max(profit, cooldown)
            else:
                sell = prices[i] + dfs(i + 2, True)
                cooldown = dfs(i + 1, False)
                dp[(i, buy)] = max(sell, cooldown)
                
            return dp[(i, buy)]

        return dfs(0, True)
